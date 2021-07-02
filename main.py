import logging
from collections import defaultdict
from typing import List, Optional, Tuple

import uvicorn
from backend.db import seed_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.domain import SeattleTeamDraft, Team, OriginalTeamOptimization
from backend.domain.frontend_interface import FrontendInterface
from backend.domain.optimization_parameters import OptimizationParameters
from backend.optimize.main import run_draft

log = logging.getLogger(__name__)

# Seed the DB and run the app
MemDB = seed_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def ping():
    return {"Hello World"}

@app.get("/data", response_model=List[Team])
def data():
    return MemDB.teams

@app.post("/optimize")
def optimize(frontend_data: FrontendInterface):
    optimization_params = OptimizationParameters(team_optimization_parameters={}, financial_metric="", performance_metric="", dont_consider_ufas=True)
    optimization_params.load_from_data(frontend_data, MemDB.teams)
    existing_team_draft, seattle_team_draft = run_draft(
        MemDB.teams, optimization_params
    )
    return {
        "original_teams": existing_team_draft,
        "seattle": seattle_team_draft,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)