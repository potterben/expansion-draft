import logging
from typing import List, Tuple

from backend.domain import Team, TeamName
from backend.domain.optimization_parameters import OptimizationParameters
from backend.domain.team import SeattleTeamDraft, TeamDraft
from backend.optimize.existing_team import get_existing_team_draft_decisions
from backend.optimize.seattle_draft import get_seattle_draft_decisions

log = logging.getLogger(__name__)


def run_draft(
    teams: List[Team], params: OptimizationParameters
) -> Tuple[List[TeamDraft], SeattleTeamDraft]:
    """Optimize the decisions for all teams."""
    # Get results for the existing teams.
    log.info("Getting Existing Team Decisions")
    existing_team_exposures = [
        get_existing_team_draft_decisions(team, params[team.name]) for team in teams
    ]

    seatle_draft_decisions = get_seattle_draft_decisions(
        existing_team_exposures, params[TeamName.SEA]
    )

    return existing_team_exposures, seatle_draft_decisions
