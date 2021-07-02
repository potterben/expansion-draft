from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName

@dataclass
class SeattleSummary:
    rowname: str
    age: float
    ps: float
    gaps: float
    ea_rating: float
    cap_hit_20_21: float
    cap_hit_21_22: float
    cap_hit_total: float

@dataclass
class SeattleTeamDraft:
    name: TeamName
    goalies: List[Player]
    defensemen: List[Player]
    forwards: List[Player]
    summary: List[SeattleSummary]

@dataclass
class OriginalTeamOptimization:
    name: TeamName
    # Protected by position
    goalies: List[Player]
    defensemen: List[Player]
    forwards: List[Player]

    exposed: List[Player]


class Team(BaseModel):
    name: TeamName
    goalies: List[Player]
    defensemen: List[Player]
    forwards: List[Player]

    @property
    def players(self):
        return self.goalies + self.defensemen + self.forwards

    @property
    def skaters(self):
        return self.defensemen + self.forwards
