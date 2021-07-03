import logging
from typing import List, Tuple
from fastapi import HTTPException

from backend.domain import Team, TeamName
from backend.domain.optimization_parameters import OptimizationParameters
from backend.domain.team import SeattleTeamDraft, OriginalTeamOptimization
from backend.optimize.existing_team import get_existing_team_draft_decisions
from backend.optimize.seattle_draft import get_seattle_draft_decisions

log = logging.getLogger(__name__)


def run_draft(
    teams: List[Team], params: OptimizationParameters
) -> Tuple[List[OriginalTeamOptimization], SeattleTeamDraft]:
    """Optimize the decisions for all teams."""
    # Get results for the existing teams.
    log.info("Getting Existing Team Decisions")
    
    existing_team_exposures = []
    for team in teams:
        try:
            existing_team_exposures.append(
                get_existing_team_draft_decisions(team, params.team_optimization_parameters[team.name]))
        except:
            raise HTTPException(status_code=500, 
                detail=f"The model for {team.name} is infeasible. Make sure your protections do not conflict with exposure requirements.")
    
    try:
        seatle_draft_decisions = get_seattle_draft_decisions(
            existing_team_exposures, params
        )
    except:
        raise HTTPException(status_code=500,
            detail="The Seattle model is infeasible. Make sure you do not keep a player for Seattle that you also protect for their existing team.")

    return existing_team_exposures, seatle_draft_decisions
