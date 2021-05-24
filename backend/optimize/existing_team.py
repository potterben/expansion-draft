import logging
from typing import List, Optional

import pulp

from backend.domain import Player, Team, TeamDraft, TeamOptimizationParameters

AGE_WEIGHT = 0.3
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

    # vs is the performance metric
    # ws is the financial metric
    # TODO get these from params
    beta = 1  # User input weight between objectives.
    perf_metric = "ea_rating"
    fin_metric = "cap_hit_total_scaled"
    user_protections: List[Player] = []
    user_exposures: List[Player] = []
    expose_ufa: bool = False

    # TODO put into team models
    player_ids = [player.id for player in team.players]

    model = pulp.LpProblem("nhl", pulp.LpMinimize)

    protect_var = pulp.LpVariable.dicts("player_id", player_ids, cat="Binary")
    max_exposed_value = pulp.LpVariable(
        "max_exposed_value"
    )  # TODO figure out if this name is correct

    # Objective Function
    max_exposed_forward_value = pulp.LpVariable("max_exposed_forward_value")
    max_exposed_defence_value = pulp.LpVariable("max_exposed_defence_value")
    max_exposed_goalie_value = pulp.LpVariable("max_exposed_goalie_value")
    ufa = pulp.LpVariable("ufa")  # TODO figure out what this variable does.

    # Add max exposed value to objective functions
    model += M * (
        max_exposed_forward_value
        + max_exposed_defence_value
        + max_exposed_goalie_value
        + 10 * max_exposed_value
    )

    # TODO figure out how to rework this part of the objective figure out if needed.
    # model += pulp.lpSum([(beta * vi - (1-beta) * wi + age_weight * (40-ai)) * (1-players[yi]) * (1-ei) + 100000 * ufa  \
    #     for vi, wi, ai, yi,ei in zip(vs, ws, age, playerNames, userExpose)])
    # max exposed value constraint
    for player in team.players:
        if not player.meets_req:
            continue

        player_value_constr = (
            beta * player.metrics[perf_metric]
            - (1 - beta) * player.contract[fin_metric]
            + AGE_WEIGHT * (40 - player.age) * (1 - protect_var[player.id])
        )

        if player.goalie:
            model += max_exposed_goalie_value - player_value_constr >= 0

        if player.defence:
            model += max_exposed_defence_value - player_value_constr >= 0

        if player.forward:
            model += max_exposed_forward_value - player_value_constr >= 0

        model += max_exposed_value - player_value_constr >= 0

    # Must protect one goalie
    goalies_constraint = pulp.lpSum([protect_var[player.id] for player in team.goalies])
    model += goalies_constraint == 1, "Goalies"

    if eight_skaters:
        skaters_constraint = pulp.lpSum(
            [protect_var[player.id] for player in team.defencemen]
        )
        model += skaters_constraint == 8, "Defenders"

    else:
        # Must protect 3 Defenders
        defenders_constraint = pulp.lpSum(
            [protect_var[player.id] for player in team.defencemen]
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
        [(1 - protect_var[player.id]) for player in team.defencemen if player.meets_req]
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

    # Don't Select UFAs if the user specifies.
    # Must expose ufa if the user specifies
    if expose_ufa:
        ufa_constraint = pulp.lpSum(
            protect_var[player.id] for player in team.players if player.contract.ufa
        )
        model += ufa_constraint - ufa == 0

    # TODO turn of reporting when solving
    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


def get_existing_team_draft_decisions(
    team: Team, params: TeamOptimizationParameters
) -> TeamDraft:
    """Returns a the teams optimize decisions under the given optimization parameters.."""

    def model_results_to_team_draft(model: pulp.LpProblem, team: Team) -> TeamDraft:
        decision_variables = model.variablesDict()
        protected_players = []
        exposed_players = []
        for player in team.players:
            var_id = f"player_id_{player.id}"
            # TODO figure out why some players varaibles are missing.
            if (var_id in decision_variables) and (
                decision_variables[var_id].varValue > 0.5
            ):
                protected_players.append(player)
            else:
                exposed_players.append(player)

        return TeamDraft(team.name, protected_players, exposed_players)

    protect_8_skaters_model = optimize_existing_protection_scenario(team, params, True)
    protect_3_defenders_7_forwards_model = optimize_existing_protection_scenario(
        team, params, True
    )

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
