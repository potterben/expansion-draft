import logging
from typing import List, Optional

import pulp

from backend.domain import Player, Team, OriginalTeamOptimization, TeamOptimizationParameters

AGE_WEIGHT_DEFAULT = 0.05
M = 2000

log = logging.getLogger(__name__)


def optimize_existing_protection_scenario(
    team: Team,
    params: Optional[TeamOptimizationParameters] = None,
    eight_skaters: bool = False,
) -> pulp.LpProblem:
    """
    Optimizes the protection decisions for a given team under the given protection decision:
        8 skaters vs. 7 forwards and 3 defenders.
    :param team: Team object to optimize over.
    :param params: Optimization parameters for the given team
    :param eight_skaters: bool if true protect 8 skaters else protect 3 defenders and 7 forwards
    :return:
    """
    log.info(f"Optimizing protection decisions for {team.name}")

    beta = params.beta  # User input weight between objectives.
    perf_metric = params.performance_metric+"_standard"
    fin_metric = params.financial_metric+"_standard"
    user_protections = params.user_protected_players
    user_exposures = params.user_exposed_players
    expose_ufa = params.dont_consider_ufas
    adjust_for_age = params.adjust_for_age

    if adjust_for_age:
        age_weight = AGE_WEIGHT_DEFAULT
    else:
        age_weight = 0

    player_ids = [player.id for player in team.players]

    model = pulp.LpProblem("nhl", pulp.LpMinimize)

    protect_var = pulp.LpVariable.dicts("player_id", player_ids, cat="Binary")
    max_exposed_value = pulp.LpVariable("max_exposed_value")

    # Objective Function

    def player_value_var_primary(player):
        if player.must_protect == "Waived":
            return 0
        if expose_ufa and player.ufa:
            return 0
        return ((player[perf_metric] + age_weight * (40 - player.age)) 
                * (1 - protect_var[player.id]))

    def player_value_var_secondary(player):
        if player.must_protect == "Waived":
            return 0
        if expose_ufa and player.ufa:
            return 0
        return (((1-beta) * player[perf_metric] - beta * player[fin_metric] + age_weight * (40 - player.age)) 
                * (1 - protect_var[player.id]))

    # Add max exposed value to objective functions
    model += M * max_exposed_value + sum( player_value_var_secondary(player) for player in team.players)

    for player in team.players:

        player_value_constr = player_value_var_primary(player)

        model += max_exposed_value - player_value_constr >= 0

    # Must protect one goalie
    goalies_constraint = pulp.lpSum([protect_var[player.id] for player in team.goalies])
    model += goalies_constraint == 1, "Goalies"

    if eight_skaters:
        skaters_constraint = pulp.lpSum(
            [protect_var[player.id] for player in team.skaters]
        )
        model += skaters_constraint == 8, "Skaters"

    else:
        # Must protect 3 Defenders
        defenders_constraint = pulp.lpSum(
            [protect_var[player.id] for player in team.defensemen]
        )
        model += defenders_constraint == 3, "Defenders"

        # Must protect 7 Forwards
        forwards_constraint = pulp.lpSum(
            [protect_var[player.id] for player in team.forwards]
        )
        model += forwards_constraint == 7, "Forwards"

    # Must expose at least 1 Goalie meeting the requirements
    expose_goalie_constraint = pulp.lpSum(
        [(1 - protect_var[player.id]) for player in team.goalies if player.meets_req]
    )
    model += expose_goalie_constraint >= 1, "ExposeGoalies"

    # Must expose at least 1 Defender meeting the requirements
    expose_defencemen_constraint = pulp.lpSum(
        [(1 - protect_var[player.id]) for player in team.defensemen if player.meets_req]
    )
    model += expose_defencemen_constraint >= 1, "ExposeDefenders"

    # Must expose atleast 2 Forwards meeting the requirements
    expose_forward_constraint = pulp.lpSum(
        [(1 - protect_var[player.id]) for player in team.forwards if player.meets_req]
    )
    model += expose_forward_constraint >= 2, "ExposeForwards"

    # Must protect players specified by the user
    # TODO just set the value of the variables to 1
    user_protection_constraint = pulp.lpSum(
        [protect_var[player.id] for player in user_protections]
    )
    model += user_protection_constraint == len(user_protections)

    # Must expose players specified by the user
    user_exposure_constraint = pulp.lpSum(
        [protect_var[player.id] for player in user_exposures]
    )
    model += user_exposure_constraint == 0

    # Don't consider UFAs if the user specifies.
    # Must expose ufa if the user specifies
    # if expose_ufa:
    #     ufa_constraint = pulp.lpSum(
    #         protect_var[player.id] for player in team.players if player.ufa
    #     )
    #     model += ufa_constraint == 0

    #model.solve(pulp.COIN_CMD(msg=False))
    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


def get_existing_team_draft_decisions(
    team: Team, params: TeamOptimizationParameters
) -> OriginalTeamOptimization:
    """Returns a the teams optimize decisions under the given optimization parameters.."""

    def model_results_to_team_draft(model: pulp.LpProblem, team: Team) -> OriginalTeamOptimization:
        decision_variables = model.variablesDict()
        protected_goalies = []
        protected_defensemen = []
        protected_forwards = []
        exposed = []
        for player in team.players:
            var_id = f"player_id_{player.id}"
            # TODO figure out why some players varaibles are missing.
            if (var_id in decision_variables) and (decision_variables[var_id].varValue > 0.5):
                if player.goalie:
                    protected_goalies.append(player)
                elif player.defence:
                    protected_defensemen.append(player)
                elif player.forward:
                    protected_forwards.append(player)
            else:
                exposed.append(player)

        return OriginalTeamOptimization(team.name, goalies=protected_goalies, defensemen=protected_defensemen, forwards=protected_forwards, exposed=exposed)

    protect_8_skaters_model = optimize_existing_protection_scenario(team, params, True)
    protect_3_defenders_7_forwards_model = optimize_existing_protection_scenario(team, params, False)

    if (protect_8_skaters_model.status != 1) and (
        protect_3_defenders_7_forwards_model.status != 1
    ):
        log.warning(
            f"Both optimization scenarios for {team.name} are infeasible"
        )  # TODO investiagte this.
        return None
        # raise AttributeError(f"Both optimization scenarios for {team.name} are infeasible")

    if protect_8_skaters_model.status != 1:
        return model_results_to_team_draft(protect_3_defenders_7_forwards_model, team)

    if protect_3_defenders_7_forwards_model.status != 1:
        return model_results_to_team_draft(protect_8_skaters_model, team)

    if (
        protect_8_skaters_model.objective.value()
        <= protect_3_defenders_7_forwards_model.objective.value()
    ):
        return model_results_to_team_draft(protect_8_skaters_model, team)
    else:
        return model_results_to_team_draft(protect_3_defenders_7_forwards_model, team)
