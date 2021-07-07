from typing import List, Dict

from pydantic import BaseModel

class OriginalTeamFrontend(BaseModel):
    beta: float
    protected: Dict[str, List[str]]
    exposed: Dict[str, List[str]]
    index: int

class SeattleFrontend(BaseModel):
    alpha: float
    keep: Dict[str, List[str]]
    remove: Dict[str, List[str]]

class FrontendInterface(BaseModel):
    seattle: SeattleFrontend
    financial_metric: str
    performance_metric: str
    original_teams: List[OriginalTeamFrontend]
    dont_consider_ufas: bool
    adjust_for_age: bool
