import logging
from typing import List

from backend.domain import Team
from backend.domain.optimization_parameters import OptimizationParameters
from backend.domain.team import TeamDraft
from backend.optimize.existing_team import get_existing_team_draft_decisions

log = logging.getLogger(__name__)


def run_draft(params: OptimizationParameters, teams: List[Team]) -> List[TeamDraft]:
    """Optimize the decisions for all teams."""
    # Get results for the existing teams.
    log.info("Getting Existing Team Decisions")
    existing_team_exposures = [
        get_existing_team_draft_decisions(team, params[team.name]) for team in teams
    ]

    return existing_team_exposures
