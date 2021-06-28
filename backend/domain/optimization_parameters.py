from typing import Dict, List, Optional

from pydantic import BaseModel

from .player import Player
from .team_name import TeamName
from .frontend_interface import SeattleFrontend, FrontendInterface
from .team import Team

class TeamOptimizationParameters(BaseModel):
    beta: float
    user_protected_players: List[Player]
    user_exposed_players: List[Player]
    financial_metric: str
    performance_metric: str
    dont_consider_ufas = bool

class SeattleParameters(BaseModel):
    alpha: float
    players_to_remove: List[Player]
    players_to_keep: List[Player]

class OptimizationParameters(BaseModel):
    team_optimization_parameters: Dict[TeamName, TeamOptimizationParameters]
    financial_metric: str
    performance_metric: str
    dont_consider_ufas: bool
    seattle_parameters: Optional[SeattleParameters] = None

    def load_from_data(self, frontendData: FrontendInterface, teamData: Dict[TeamName, Team]) -> None:
        # Copy over frontend metrics
        self.financial_metric = frontendData.financial_metric
        self.performance_metric = frontendData.performance_metric
        self.dont_consider_ufas = frontendData.dont_consider_ufas

        # Make a keep and remove set so we can find the players to keep and remove when iterating over all the players
        keep_set = set()
        keep_list = []
        for player_ids in frontendData.seattle.keep.values():
            for player_id in player_ids:
                keep_set.add(player_id)
        remove_set = set()
        remove_list = []
        for player_ids in frontendData.seattle.remove.values():
            for player_id in player_ids:
                remove_set.add(player_id)

        # Parse protected and exposed players
        for team in frontendData.original_teams:
            optimization_parameters = TeamOptimizationParameters(
                beta=(team.beta) / 100,  # TODO sync def of beta with front end
                user_protected_players=[],
                user_exposed_players=[],
                financial_metric=self.financial_metric,
                performance_metric=self.performance_metric,
                dont_consider_ufas=self.dont_consider_ufas,
            )
            
            current_team_players = teamData[team.index].players
            team_name = teamData[team.index].name

            protected_set = set()
            for player_ids in team.protected.values():
                for player_id in player_ids:
                    protected_set.add(player_id)
            exposed_set = set()
            for player_ids in team.exposed.values():
                for player_id in player_ids:
                    exposed_set.add(player_id)

            for player in current_team_players:
                if player.id in exposed_set:
                    optimization_parameters.user_exposed_players.append(player)
                if player.id in protected_set:
                    optimization_parameters.user_protected_players.append(player)
                if player.id in keep_set:
                    keep_list.append(player)
                if player.id in remove_set:
                    remove_list.append(player)

            self.team_optimization_parameters[team_name] = optimization_parameters
        
        seattle_parameters = SeattleParameters(
                                alpha = (frontendData.seattle.alpha/ 100),
                                players_to_remove=remove_list,
                                players_to_keep=keep_list)

        self.seattle_parameters = seattle_parameters