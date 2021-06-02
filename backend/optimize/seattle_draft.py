import logging
from typing import Optional

import pulp

from backend.domain import (
    SeattleTeamDraft,
    TeamDraft,
    TeamOptimizationParameters,
)

AGE_WEIGHT = 0.3


log = logging.getLogger(__name__)


def optimize_seattle_selection_scenario(
    existing_teams_draft: TeamDraft,
    params: Optional[TeamOptimizationParameters] = None,
) -> pulp.LpProblem:

    """Optimizes the selection decisions for Seattle.
    :param params: Optimization parameters for Seattle
    :param existing_teams_draft: TeamDraft object for each existing team containing name, protections, and exposures
    :return:
    """
    log.info(f"Optimizing selection decisions for Seattle")

    # TODO get these from params
    if params is None:
        alpha = 0.5  # User input weight between objectives.
        perf_metric = "ea_rating"
        fin_metric = "cap_hit_total_scaled"
    else:
        alpha = params.alpha
        perf_metric = params.perf
        fin_metric = "cap_hit_total_scaled"

    # TODO put into team models
    exposed_ids = [player.id for player in existing_teams_draft.exposed_players]

    model = pulp.LpProblem("nhl", pulp.LpMaximize)

    select_var = pulp.LpVariable.dicts("player_id", exposed_ids, cat="Binary")

    # Objective
    perf_obj = pulp.lpSum(
        [
            player.metrics[perf_metric]
            for player in existing_teams_draft.exposed_players
            if select_var[player.id]
        ]
    )
    fin_obj = pulp.lpSum(
        [
            player.contract[fin_metric]
            for player in existing_teams_draft.exposed_players
            if select_var[player.id]
        ]
    )
    age_obj = pulp.lpSum(
        [
            player.age
            for player in existing_teams_draft.exposed_players
            if select_var[player.id]
        ]
    )

    model += (1 - alpha) * perf_obj - alpha * fin_obj - AGE_WEIGHT * age_obj

    # Select 1 player from each existing team
    for team in existing_teams_draft.team:
        select_team_player_constraint = pulp.lpSum(
            [select_var[player.id] for player in existing_teams_draft.exposed_players]
        )
        model += select_team_player_constraint == 1, "SelectPlayer_" + str(team)

    # Select at least 14 F, 9 D, 3 G
    select_F_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.forward
        ]
    )
    model += select_F_constraint >= 14, "SelectForward"

    select_D_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.defence
        ]
    )
    model += select_D_constraint >= 9, "SelectDefence"

    select_G_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.goalie
        ]
    )
    model += select_G_constraint == 3, "SelectGoalie"

    # Select at least 18 skaters, 2 G under contract next year
    select_skater_contract_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if ((player.forward or player.defence) and player.under_ct)
        ]
    )
    model += select_skater_contract_constraint >= 18, "SelectContractSkater"

    select_G_contract_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if (player.goalie and player.under_ct)
        ]
    )
    model += select_G_contract_constraint >= 2, "SelectContractGoalie"

    # minimum and maximum team cap hit
    select_caphit_constraint = pulp.lpSum(
        [
            player.contract["cap_hit_20_21"]
            for player in existing_teams_draft.exposed_players
            if select_var[player.id]
        ]
    )
    # TODO check 60-100% team cap
    model += select_caphit_constraint >= 50, "SelectMinCapHit"
    model += select_caphit_constraint <= 80, "SelectMaxCapHit"

    # select at least 4 C, 4 LW, 4 RW
    select_C_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.center
        ]
    )
    model += select_C_constraint >= 4, "SelectC"

    select_LW_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.left_wing
        ]
    )
    model += select_LW_constraint >= 4, "SelectLW"

    select_RW_constraint = pulp.lpSum(
        [
            select_var[player.id]
            for player in existing_teams_draft.exposed_players
            if player.right_wing
        ]
    )
    model += select_RW_constraint >= 4, "SelectRW"

    # TODO turn of reporting when solving
    model.solve(pulp.PULP_CBC_CMD(msg=0))

    return model


def get_seattle_draft_decisions(
    params: TeamOptimizationParameters, existing_teams_draft: TeamDraft
) -> SeattleTeamDraft:
    """Returns seattle decisions under the given optimization parameters."""

    def model_results_to_seattle_draft(
        model: pulp.LpProblem, existing_teams_draft: TeamDraft
    ) -> SeattleTeamDraft:
        decision_variables = model.variablesDict()
        selected_players = []
        for player in existing_teams_draft.exposed_players:
            var_id = f"player_id_{player.id}"
            # TODO figure out why some players variables are missing.
            if (var_id in decision_variables) and (
                decision_variables[var_id].varValue > 0.5
            ):
                selected_players.append(player)

        return SeattleTeamDraft("Kraken", selected_players)

    seattle_selection_model = optimize_seattle_selection_scenario(
        params, existing_teams_draft
    )

    return model_results_to_seattle_draft(seattle_selection_model, existing_teams_draft)