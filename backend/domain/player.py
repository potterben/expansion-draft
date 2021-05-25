from pydantic import BaseModel

from .team_name import TeamName


# TODO update this with new data
class PlayerContract(BaseModel):
    cap_hit_20_21: float
    cap_hit_21_22: float
    cap_hit_22_23: float
    cap_hit_23_24: float
    cap_hit_24_25: float
    cap_hit_25_26: float
    cap_hit_total: float
    cap_hit_17_18_scaled: float
    cap_hit_total_scaled: float
    ufa_expiry: int  # year the player is a ufa
    rfa_expiry: int  # year the player is an rfa
    expiry: str  # yeah the player contract expires
    ufa: bool

    def __getitem__(self, item):
        return getattr(self, item)


# TODO update this with new data
class PlayerMetrics(BaseModel):
    ps_16_17: float
    ps_15_16: float
    ps_14_15: float
    ps_avg: float
    gaps_16_17: float
    gaps_15_16: float
    gaps_14_15: float
    gvt_15_16: float
    gvt_14_15: float
    gvt_avg: float
    ea_rating: int
    ps_16_17_scaled: float
    ps_15_16_scaled: float
    ps_14_15_scaled: float
    ps_avg_scaled: float
    gaps_16_17_scaled: float
    gaps_15_16_scaled: float
    gaps_14_15_scaled: float
    gvt_15_16_scaled: float
    gvt_14_15_scaled: float
    gvt_avg_scaled: float
    ea_rating_scaled: float

    def __getitem__(self, item):
        return getattr(self, item)


class Player(BaseModel):
    id: str
    first_name: str
    last_name: str
    name: str
    team: TeamName
    position: str
    age: int
    contract: PlayerContract
    metrics: PlayerMetrics
    forward: bool
    defence: bool
    goalie: bool
    center: bool
    right_wing: bool
    left_wing: bool
    gp_16_17: float
    gp_15_16: float
    gp_14_15: float
    nmc: bool
    game_req: bool
    must_protect: bool
    meets_req: bool
    under_ct: bool
    protected_irl: bool
    protected_cf: bool
    protected_tsn: bool

    @property
    def var_id(self):
        return f"player_id_{self.id}"
