from typing import Dict, List

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName
from .frontend_interface import FrontendInterface
from .team import Team

class TeamOptimizationParameters(BaseModel):
    beta: float
    user_protected_players: List[Player]
    user_exposed_players: List[Player]
    financial_metric: str
    performance_metric: str

class OptimizationParameters(BaseModel):
    team_optimization_parameters: Dict[TeamName, TeamOptimizationParameters]
    financial_metric: str
    performance_metric: str
    alpha: float

    def load_from_data(self, frontendData: FrontendInterface, teamData: Dict[TeamName, Team]) -> None:
        # Copy over frontend metrics
        self.financial_metric = frontendData.financial_metric
        self.performance_metric = frontendData.performance_metric
        self.alpha = frontendData.alpha
        
        # Parse protected and exposed players
        for team in frontendData.original_teams:
            optimization_parameters = TeamOptimizationParameters(
                beta=(100 - team.beta) / 100,  # TODO sync def of beta with front end
                user_protected_players=[],
                user_exposed_players=[],
                financial_metric=self.financial_metric,
                performance_metric=self.performance_metric,
            )
            
            current_team_players = teamData[team.index].players
            team_name = teamData[team.index].name

            protected_set = set()
            for player_ids in team.protected.values():
                for player_id in player_ids:
                    protected_set.add(player_id)
            for player in current_team_players:
                if player.id in protected_set:
                    optimization_parameters.user_protected_players.append(player)
            
            exposed_set = set()
            for player_ids in team.exposed.values():
                for player_id in player_ids:
                    exposed_set.add(player_id)
            for player in current_team_players:
                if player.id in exposed_set:
                    optimization_parameters.user_exposed_players.append(player)
            self.team_optimization_parameters[team_name] = optimization_parameters