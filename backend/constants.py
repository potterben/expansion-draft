from pathlib import Path

from backend.domain import TeamName

PROJECT_DIR = Path(__file__).parent.parent
PLAYER_CSV = PROJECT_DIR / "data" / "Player_Master_Auto.csv"
SUMMARY_CSV = PROJECT_DIR / "data" / "Summary_Master_Auto.csv"

EXISTING_TEAMS = [team for team in TeamName if team != TeamName.SEA]
