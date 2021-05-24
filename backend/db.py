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
            cap_hit_16_17=row["CH 16-17"],
            cap_hit_17_18=row["CH 17-18"],
            cap_hit_18_19=row["CH 18-19"],
            cap_hit_19_20=row["CH 19-20"],
            cap_hit_20_21=row["CH 20-21"],
            cap_hit_21_22=row["CH 21-22"],
            cap_hit_22_23=row["CH 22-23"],
            cap_hit_23_24=row["CH 23-24"],
            cap_hit_24_25=row["CH 24-25"],
            cap_hit_25_26=row["CH 25-26"],
            cap_hit_total=row["CH Total"],
            cap_hit_17_18_scaled=row["CH 17-18_Scaled"],
            cap_hit_total_scaled=row["CH Total_Scaled"],
            ufa_expiry=row["UFA Expiry"],
            rfa_expiry=row["RFA Expiry"],
            expiry=row["Expiry"],
            ufa=row["UFA"],
        )
        metrics = PlayerMetrics(
            ps_16_17=row["PS 16-17"],
            ps_15_16=row["PS 15-16"],
            ps_14_15=row["PS 14-15"],
            ps_avg=row["PS Avg"],
            gaps_16_17=row["GAPS 16-17"],
            gaps_15_16=row["GAPS 15-16"],
            gaps_14_15=row["GAPS 14-15"],
            gvt_15_16=row["GVT 15-16"],
            gvt_14_15=row["GVT 14-15"],
            gvt_avg=row["GVT Avg"],
            ea_rating=row["OVR"],
            ps_16_17_scaled=row["PS 16-17_Scaled"],
            ps_15_16_scaled=row["PS 15-16_Scaled"],
            ps_14_15_scaled=row["PS 14-15_Scaled"],
            ps_avg_scaled=row["PS Avg_Scaled"],
            gaps_16_17_scaled=row["GAPS 16-17_Scaled"],
            gaps_15_16_scaled=row["GAPS 15-16_Scaled"],
            gaps_14_15_scaled=row["GAPS 14-15_Scaled"],
            gvt_15_16_scaled=row["GVT 15-16_Scaled"],
            gvt_14_15_scaled=row["GVT 14-15_Scaled"],
            gvt_avg_scaled=row["GVT Avg_Scaled"],
            ea_rating_scaled=row["OVR_Scaled"],
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
            gp_16_17=row["GP 16-17"],
            gp_15_16=row["GP 15-16"],
            gp_14_15=row["GP 14-15"],
            nmc=row["NMC"],
            game_req=row["Game Req"],
            must_protect=row["Must Protect"],
            meets_req=row["Meets Exposure"],
            under_ct=row["Under Contract 17/18"],
            # Protection Data
            protected_irl=row["Protected_Official"],
            protected_cf=row["Protected_CF"],
            protected_tsn=row["Protected_TSN"],
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
