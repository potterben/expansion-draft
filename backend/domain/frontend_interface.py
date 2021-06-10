from typing import List, Dict

from pydantic import BaseModel

class OriginalTeamFrontend(BaseModel):
    beta: float
    protected: Dict[str, List[str]]
    exposed: Dict[str, List[str]]
    index: int

class FrontendInterface(BaseModel):
    alpha: float
    financial_metric: str
    performance_metric: str
    original_teams: List[OriginalTeamFrontend]