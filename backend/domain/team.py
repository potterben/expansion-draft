from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName


@dataclass
class SeattleTeamDraft:
    name: TeamName
    goalies: List[Player]
    defensemen: List[Player]
    forwards: List[Player]
    #summary: 

@dataclass
class SeattleSummary:
    position_name: str
    ps: float
    pspg: float
    ea: float
    cap_hit_21_22: float
    cap_hit_total: float

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
