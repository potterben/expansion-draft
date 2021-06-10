from pydantic import BaseModel

from .team_name import TeamName

class Player(BaseModel):
    id: str
    first_name: str
    last_name: str
    name: str
    team: TeamName
    position: str
    age: int

    cap_hit_20_21: float
    cap_hit_21_22: float
    cap_hit_22_23: float
    cap_hit_23_24: float
    cap_hit_24_25: float
    cap_hit_25_26: float
    cap_hit_26_27: float
    cap_hit_total: float
    cap_percent: float
    # scaled metrics to same scale as cap hit 21-22
    cap_hit_21_22_scaled: float
    cap_hit_total_scaled: float
    ufa_expiry: int  # year the player is a ufa
    rfa_expiry: int  # year the player is an rfa
    expiry: str  # year the player contract expires
    ufa: bool

    forward: bool
    defence: bool
    goalie: bool
    center: bool
    right_wing: bool
    left_wing: bool
    right_def: bool
    left_def: bool
    gp: float
    nmc: bool
    game_req: bool
    must_protect: bool
    meets_req: bool
    under_ct: bool

    # offensive PS, defensive PS, PS
    ops: float
    dps: float
    ps: float
    # game-adjusted metrics
    gaops: float
    gadps: float
    gaps: float
    # ratings from NHL 2021
    ea_rating: float
    # scaled metrics to same scale as cap hit 21-22
    ops_scaled: float
    dps_scaled: float
    ps_scaled: float
    gaops_scaled: float
    gadps_scaled: float
    gaps_scaled: float
    ea_rating_scaled: float

    @property
    def var_id(self):
        return f"player_id_{self.id}"

    def __getitem__(self, item):
        return getattr(self, item)
