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
    cap_hit_total: float
    # standardized metrics
    cap_hit_20_21_standard: float
    cap_hit_21_22_standard: float
    cap_hit_total_standard: float
    # other contract info
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

    # Point shares, game adjusted point shares, ea 2021 ratings
    ps: float
    gaps: float
    ea_rating: float
    # standardized performance information
    ps_standard: float
    gaps_standard: float
    ea_rating_standard: float

    @property
    def var_id(self):
        return f"player_id_{self.id}"

    def __getitem__(self, item):
        return getattr(self, item)
