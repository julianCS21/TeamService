from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.infraestructure.inbound.TeamController import team_router
application = FastAPI()
application.include_router(team_router, prefix="/api/v1/teams")
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
