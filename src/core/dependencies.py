from fastapi import Depends
from src.core.config import Settings
from src.infraestructure.outbound.externalClients.TeamClient import TeamClient
from src.application.TeamService import TeamService


def get_settings() -> Settings:
    return Settings()


def get_team_client(settings: Settings = Depends(get_settings)) -> TeamClient:
    return TeamClient(settings)


def get_team_service(team_client: TeamClient = Depends(get_team_client)) -> TeamService:
    return TeamService(team_client)

