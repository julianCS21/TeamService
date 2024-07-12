from fastapi import FastAPI
from src.infraestructure.inbound.TeamController import team_router
application = FastAPI()
application.include_router(team_router, prefix="/api/v1/teams")
