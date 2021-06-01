from typing import Dict, List

import pandas as pd

from backend.constants import EXISTING_TEAMS, PLAYER_CSV
from backend.domain import Player, PlayerContract, PlayerMetrics, Team, TeamName


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
        contract = PlayerContract(
            cap_hit_20_21=row["CH 20-21"],
            cap_hit_21_22=row["CH 21-22"],
            cap_hit_22_23=row["CH 22-23"],
            cap_hit_23_24=row["CH 23-24"],
            cap_hit_24_25=row["CH 24-25"],
            cap_hit_25_26=row["CH 25-26"],
            cap_hit_26_27=row["CH 26-27"],
            cap_hit_total=row["CH Total"],
            cap_percent=row["Cap%"],
            cap_hit_21_22_scaled=row["CH 21-22_scaled"],
            cap_hit_total_scaled=row["CH Total_scaled"],
            ufa_expiry=row["UFA Expiry"],
            rfa_expiry=row["RFA Expiry"],
            expiry=row["Expiry"],
            ufa=row["UFA"],
        )
        metrics = PlayerMetrics(
            ops=row["OPS"],
            dps=row["DPS"],
            ps=row["PS"],
            gaops=row["GAOPS"],
            gadps=row["GADPS"],
            gaps=row["GAPS"],
            ea_rating=row["Overall"],
            ops_scaled=row["OPS_scaled"],
            dps_scaled=row["DPS_scaled"],
            ps_scaled=row["PS_scaled"],
            gaops_scaled=row["GAOPS_scaled"],
            gadps_scaled=row["GADPS_scaled"],
            gaps_scaled=row["GAPS_scaled"],
            ea_rating_scaled=row["Overall_scaled"],
        )

        player = Player(
            id=str(idx),
            first_name=row["First Name"],
            last_name=row["Last Name"],
            name=row["Player"],
            team=TeamName(row["Team"]),
            position=row["Pos"],
            age=row["Age"],
            contract=contract,
            metrics=metrics,
            forward=row["F"],
            defence=row["D"],
            goalie=row["G"],
            center=row["C"],
            right_wing=row["RW"],
            left_wing=row["LW"],
            right_def=row["RD"],
            left_def=row["LD"],
            gp=row["GP"],
            nmc=row["NMC"],
            game_req=row["Game Req"],
            must_protect=row["Must Protect"],
            meets_req=row["Meets Exposure"],
            under_ct=row["Under Contract 21/22"],
            # Protection Data
            #protected_irl=row["Protected_Official"],
            #protected_cf=row["Protected_CF"],
            #protected_tsn=row["Protected_TSN"],
        )
        players.append(player)

    teams = {
        team: Team(name=team, goalies=[], defencemen=[], forwards=[])
        for team in EXISTING_TEAMS
    }

    for player in players:
        if player.goalie:
            teams[player.team].goalies.append(player)
        elif player.defence:
            teams[player.team].defencemen.append(player)
        elif player.forward:
            teams[player.team].forwards.append(player)
        else:
            raise ValueError(f"{player} does not have a valid position!")

    return MemoryDB(players, teams)
