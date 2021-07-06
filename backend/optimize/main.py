import logging
from typing import List, Tuple
from fastapi import HTTPException

from backend.domain import Team, FigureData
from backend.domain.optimization_parameters import OptimizationParameters
from backend.domain.team import SeattleTeamDraft, OriginalTeamOptimization
from backend.optimize.existing_team import get_existing_team_draft_decisions
from backend.optimize.seattle_draft import get_seattle_draft_decisions

log = logging.getLogger(__name__)


def run_draft(
    teams: List[Team], figuredata: FigureData, params: OptimizationParameters
) -> Tuple[List[OriginalTeamOptimization], SeattleTeamDraft]:
    """Optimize the decisions for all teams."""
    # Get results for the existing teams.
    log.info("Getting Existing Team Decisions")
    
    existing_team_exposures = []
    protection_model_success = True
    for team in teams:
        team_draft_decisions = get_existing_team_draft_decisions(team, params.team_optimization_parameters[team.name])
        if team_draft_decisions == None:
            protection_model_success = False
            try:
                raise HTTPException(status_code=500, 
                 detail=f"The model for {team.name} is infeasible. Make sure your protections do not conflict with exposure requirements.")
            except:
                raise
        else:
            existing_team_exposures.append(team_draft_decisions)    
    
    if protection_model_success:
        try:
            seatle_draft_decisions = get_seattle_draft_decisions(
                existing_team_exposures, figuredata, params
            )
        except:
            raise HTTPException(status_code=500,
                detail="The Seattle model is infeasible. Make sure you do not keep a player for Seattle that you also protect for their existing team.")

    return existing_team_exposures, seatle_draft_decisions
