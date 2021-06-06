from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName


@dataclass
class SeattleTeamDraft:
    name: TeamName
    chosen_player: List[Player]


@dataclass
class TeamDraft:
    name: TeamName
    # Protected by poisition
    protected_players: List[Player]
    exposed_players: List[Player]


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
