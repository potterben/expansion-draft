import logging
from collections import defaultdict

from backend.db import seed_db
from backend.optimize.main import run_draft

log = logging.getLogger(__name__)

if __name__ == "__main__":
    MemDB = seed_db()
    mock_params = defaultdict(lambda: None)
    draft_decisions = run_draft(mock_params, MemDB.teams)
    print("Hello")
