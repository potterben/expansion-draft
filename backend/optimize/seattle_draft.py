import logging
from typing import List, Optional

import pulp

from backend.domain import (
    SeattleTeamDraft,
    OriginalTeamOptimization,
    TeamName,
    OptimizationParameters,
)

AGE_WEIGHT = 0.06


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
    fin_metric = params.financial_metric+"_standard"
    user_keep = params.seattle_parameters.players_to_keep
    user_remove = params.seattle_parameters.players_to_remove
    alpha = params.seattle_parameters.alpha  # User input weight between objectives.
    expose_ufa = params.dont_consider_ufas

    exposed_players = [
        player
        for team_draft in existing_teams_drafts
        for player in team_draft.exposed
    ]
    exposed_ids = [player.id for player in exposed_players]

    model = pulp.LpProblem("nhl", pulp.LpMaximize)

    select_var = pulp.LpVariable.dicts("player_id", exposed_ids, cat="Binary")

    # Objective

    def player_value_var(player):
        if expose_ufa and player.ufa:
            return 0
        return (((1-alpha) * player[perf_metric] - alpha * player[fin_metric] + AGE_WEIGHT * (40 - player.age)) 
                * (select_var[player.id]))

    model += sum(player_value_var(player) for player in exposed_players)

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
    model += select_caphit_constraint >= 48.9, "SelectMinCapHit"  # 60 percent of cap
    model += select_caphit_constraint <= 81.5, "SelectMaxCapHit"  # 100 percent of cpa

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

    # TODO turn of reporting when solving
    model.solve(pulp.COIN_CMD(msg=0))

    return model


def get_seattle_draft_decisions(
    existing_teams_drafts: List[OriginalTeamOptimization], params: OptimizationParameters
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

        seattle_results = SeattleTeamDraft(TeamName.SEA, goalies=[], defensemen=[], forwards=[])
        for player in selected_players:
            if player.goalie:
                seattle_results.goalies.append(player)
            elif player.defence:
                seattle_results.defensemen.append(player)
            elif player.forward:
                seattle_results.forwards.append(player)
        return seattle_results

    seattle_selection_model = optimize_seattle_selection_scenario(
        existing_teams_drafts, params
    )

    return model_results_to_seattle_draft(
        seattle_selection_model, existing_teams_drafts
    )
