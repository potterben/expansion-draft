import logging
from typing import List, Optional

import pulp

from backend.domain import (
    TeamSummary,
    SeattleTeamDraft,
    OriginalTeamOptimization,
    TeamName,
    OptimizationParameters,
    Player,
    FigureData
)

AGE_WEIGHT_DEFAULT = 0.05
M = 2000
MIN_CAP_HIT = 48.9  # 60% of cap
MAX_CAP_HIT = 81.5  # 100% of cap

log = logging.getLogger(__name__)


def optimize_seattle_selection_scenario(
    existing_teams_drafts: List[OriginalTeamOptimization],
    params: Optional[OptimizationParameters] = None,
) -> pulp.LpProblem:

    """Optimizes the selection decisions for Seattle.
    :param params: Optimization parameters for Seattle
    :param existing_teams_drafts: OriginalTeamOptimization object for each existing team containing name, protections, and exposures
    :return:
    """
    log.info(f"Optimizing selection decisions for Seattle")

    # TODO get these from params
    perf_metric = params.performance_metric+"_standard"
    fin_metric = params.financial_metric
    user_keep = params.seattle_parameters.players_to_keep
    user_remove = params.seattle_parameters.players_to_remove
    alpha = params.seattle_parameters.alpha  # User input weight between objectives.
    expose_ufa = params.dont_consider_ufas
    adjust_for_age = params.adjust_for_age

    if adjust_for_age:
        age_weight = AGE_WEIGHT_DEFAULT
    else:
        age_weight = 0

    exposed_players = [
        player
        for team_draft in existing_teams_drafts
        for player in team_draft.exposed
    ]
    exposed_ids = [player.id for player in exposed_players]

    model = pulp.LpProblem("nhl", pulp.LpMaximize)

    select_var = pulp.LpVariable.dicts("player_id", exposed_ids, cat="Binary")
    perf_obj = pulp.LpVariable("sum_of_player_performance")
    fin_obj = pulp.LpVariable("absolute_deviation_from_cap_slider_settings")

    # Objective

    model += perf_obj - M*fin_obj

    def player_value_var(player):
        if expose_ufa and player.ufa:
            return 0
        return ((player[perf_metric] + age_weight * (40 - player.age)) 
                * (select_var[player.id]))

    model += perf_obj <= pulp.lpSum([player_value_var(player) for player in exposed_players])

    fin_metric_sum = pulp.lpSum([player[fin_metric] * select_var[player.id] for player in exposed_players])
    target_cap_hit = MAX_CAP_HIT * (1-alpha) + MIN_CAP_HIT * alpha
    model += fin_obj >= fin_metric_sum - target_cap_hit, "FinObjAbs1"
    model += fin_obj >= 0

    model += pulp.lpSum([select_var[player.id] for player in user_keep]) == len(user_keep), "KeepPlayers"

    model += pulp.lpSum([select_var[player.id] for player in user_remove]) == 0, "RemovePlayers"

    # Select 1 player from each existing team
    for team in existing_teams_drafts:
        select_team_player_constraint = pulp.lpSum(
            [select_var[player.id] for player in team.exposed]
        )
        model += select_team_player_constraint == 1, "SelectPlayer_" + str(team)

    # Select at least 14 F, 9 D, 3 G
    select_F_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.forward]
    )
    model += select_F_constraint >= 14, "SelectForward"

    select_D_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.defence]
    )
    model += select_D_constraint >= 9, "SelectDefence"

    select_G_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.goalie]
    )
    model += select_G_constraint == 3, "SelectGoalie"

    # Select at least 18 skaters, 2 G under contract next year
    select_skater_contract_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in exposed_players
            if ((player.forward or player.defence) and player.under_ct)
        ]
    )
    model += select_skater_contract_constraint >= 18, "SelectContractSkater"

    select_G_contract_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in exposed_players
            if (player.goalie and player.under_ct)
        ]
    )
    model += select_G_contract_constraint >= 2, "SelectContractGoalie"

    # minimum and maximum team cap hit
    select_caphit_constraint = pulp.lpSum(
        [
            player["cap_hit_20_21"] * select_var[player.id]
            for player in exposed_players
        ]
    )
    model += select_caphit_constraint >= MIN_CAP_HIT, "SelectMinCapHit"  # 60 percent of cap
    model += select_caphit_constraint <= MAX_CAP_HIT, "SelectMaxCapHit"  # 100 percent of cap

    # select at least 4 C, 4 LW, 4 RW
    select_C_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.center]
    )
    model += select_C_constraint >= 4, "SelectC"

    select_LW_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.left_wing]
    )
    model += select_LW_constraint >= 4, "SelectLW"

    select_RW_constraint = pulp.lpSum(
        [select_var[player.id] for player in exposed_players if player.right_wing]
    )
    model += select_RW_constraint >= 4, "SelectRW"

    # Don't Select UFAs if the user specifies.
    # Must expose ufa if the user specifies
    # if expose_ufa:
    #     ufa_constraint = pulp.lpSum(
    #         select_var[player.id] for player in exposed_players if player.ufa
    #     )
    #     model += ufa_constraint == 0

    #model.solve(pulp.COIN_CMD(msg=0,timeLimit=10))
    model.solve(pulp.PULP_CBC_CMD(msg=0,timeLimit=10))

    return model


def get_seattle_draft_decisions(
    existing_teams_drafts: List[OriginalTeamOptimization], figuredata: FigureData, params: OptimizationParameters
) -> SeattleTeamDraft:
    """Returns seattle decisions under the given optimization parameters."""

    def model_results_to_seattle_draft(
        model: pulp.LpProblem, existing_teams_drafts: List[OriginalTeamOptimization]
    ) -> SeattleTeamDraft:
        decision_variables = model.variablesDict()
        exposed_players = [
            player
            for team_draft in existing_teams_drafts
            for player in team_draft.exposed
        ]
        selected_players = []
        for player in exposed_players:
            var_id = f"player_id_{player.id}"
            # TODO figure out why some players variables are missing.
            if (var_id in decision_variables) and (
                decision_variables[var_id].varValue > 0.5
            ):
                selected_players.append(player)

        seattle_results = SeattleTeamDraft(TeamName.SEA, goalies=[], defensemen=[], forwards=[], summary=[], figure=FigureData([],[],[],[],[],[],[],[]))
        for player in selected_players:
            if player.goalie:
                seattle_results.goalies.append(player)
            elif player.defence:
                seattle_results.defensemen.append(player)
            elif player.forward:
                seattle_results.forwards.append(player)

        def get_mean_stat(metric, players:List[Player]) -> float:
            denom = sum((player[metric] != 0) for player in players)
            if denom == 0:
                return 0
            return sum(player[metric] for player in players)/denom

        def get_summary(rowname:str, players:List[Player]) -> TeamSummary:
            summary = TeamSummary(rowname,age=0,ps=0,gaps=0,ea_rating=0,cap_hit_20_21=0,cap_hit_21_22=0,cap_hit_avg=0)
            summary.age             += get_mean_stat("age", players)
            summary.ps              += sum(player.ps for player in players)
            summary.gaps            += sum(player.gaps for player in players)
            summary.ea_rating       += get_mean_stat("ea_rating",players)
            summary.cap_hit_20_21   += sum(player.cap_hit_20_21 for player in players)
            summary.cap_hit_21_22   += sum(player.cap_hit_21_22 for player in players)
            summary.cap_hit_avg   += sum(player.cap_hit_avg for player in players)
            return summary
        
        forwards_summary = get_summary("Forwards",seattle_results.forwards)
        defensemen_summary = get_summary("Defensemen",seattle_results.defensemen)
        goalie_summary = get_summary("Goalies",seattle_results.goalies)
        overall_summary = get_summary("Overall",selected_players)

        seattle_results.summary += [forwards_summary, defensemen_summary, goalie_summary, overall_summary]

        seattle_results.figure.teamname = figuredata.teamname + ["SEA"]
        seattle_results.figure.age = figuredata.age + [overall_summary.age]
        seattle_results.figure.ps = figuredata.ps + [overall_summary.ps]
        seattle_results.figure.gaps = figuredata.gaps + [overall_summary.gaps]
        seattle_results.figure.ea_rating = figuredata.ea_rating + [overall_summary.ea_rating]
        seattle_results.figure.cap_hit_20_21 = figuredata.cap_hit_20_21 + [overall_summary.cap_hit_20_21]
        seattle_results.figure.cap_hit_21_22 = figuredata.cap_hit_21_22 + [overall_summary.cap_hit_21_22]
        seattle_results.figure.cap_hit_avg = figuredata.cap_hit_avg + [overall_summary.cap_hit_avg]

        return seattle_results

    seattle_selection_model = optimize_seattle_selection_scenario(
        existing_teams_drafts, params
    )

    return model_results_to_seattle_draft(
        seattle_selection_model, existing_teams_drafts
    )
