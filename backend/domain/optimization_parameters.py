from typing import Dict, List

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName


class TeamOptimizationParameters(BaseModel):
    beta: float
    financial_metric: str  # TODO make this an enum?
    perfomance_metric: str  # TODO make this an enum?
    user_protected_players: List[Player]
    user_exposed_players: List[Player]


class OptimizationParameters(BaseModel):
    team_optimization_parameters: Dict[TeamName, TeamOptimizationParameters]
