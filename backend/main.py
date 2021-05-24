import logging
from typing import List

import uvicorn
from db import seed_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.domain import Team, TeamDraft
from backend.domain.optimization_parameters import OptimizationParameters
from backend.optimize.main import run_draft

log = logging.getLogger(__name__)

# Seed the DB and run the app
MemDB = seed_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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


@app.get("/optimize", response_model=List[TeamDraft])
def draft(params: OptimizationParameters):
    return run_draft(params, MemDB.teams)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
