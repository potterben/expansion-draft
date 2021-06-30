from typing import Dict, List

import pandas as pd

from backend.constants import EXISTING_TEAMS, PLAYER_CSV
from backend.domain import Player, Team, TeamName


class MemoryDB:
    def __init__(self, players: List[Player], teams: Dict[TeamName, Team]):
        self._players: List[Player] = players
        self._teams = [t for t in teams.values()]
        self._teams_dict: teams

    @property
    def players(self):
        return self._players

    @property
    def teams(self):
        return self._teams

def seed_db() -> MemoryDB:
    players = []
    df = pd.read_csv(PLAYER_CSV, encoding="latin-1")
    for idx, row in df.T.iteritems():
        player = Player(
            id=str(idx),
            first_name=row["First Name"],
            last_name=row["Last Name"],
            name=row["Player"],
            team=TeamName(row["Team"]),
            position=row["Pos"],
            age=row["Age"],
            forward=row["F"],
            defence=row["D"],
            goalie=row["G"],
            center=row["C"],
            right_wing=row["RW"],
            left_wing=row["LW"],
            right_def=row["RD"],
            left_def=row["LD"],
            # games played
            gp=row["GP"],
            nmc=row["NMC"],
            game_req=row["Game Req"],
            must_protect=row["Must Protect"],
            meets_req=row["Meets Exposure"],
            under_ct=row["Under Contract 21/22"],

            # financial related information
            cap_hit_20_21=row["CH 20-21"],
            cap_hit_21_22=row["CH 21-22"],
            cap_hit_total=row["CH Total"],
            cap_hit_20_21_standard=row["CH 20-21_standard"],
            cap_hit_21_22_standard=row["CH 21-22_standard"],
            cap_hit_total_standard=row["CH Total_standard"],
            ufa_expiry=row["UFA Expiry"],
            rfa_expiry=row["RFA Expiry"],
            expiry=row["Expiry"],
            ufa=row["UFA"],
            
            # performance relate information
            ps=row["PS"],
            gaps=row["GAPS"],
            ea_rating=row["Overall"],
            # standardized performance information
            ps_standard = row['PS_standard'],
            gaps_standard = row['GAPS_standard'],
            ea_rating_standard = row['Overall_standard'],
        )

        players.append(player)

    teams = {
        team: Team(name=team, goalies=[], defensemen=[], forwards=[])
        for team in EXISTING_TEAMS
    }

    for player in players:
        if player.goalie:
            teams[player.team].goalies.append(player)
        elif player.defence:
            teams[player.team].defensemen.append(player)
        elif player.forward:
            teams[player.team].forwards.append(player)
        else:
            raise ValueError(f"{player} does not have a valid position!")

    return MemoryDB(players, teams)
