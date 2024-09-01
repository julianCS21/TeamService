from fastapi import APIRouter, Depends, HTTPException
from src.application.TeamService import TeamService
from src.domain.exceptions.TeamBadRequestException import TeamBadRequestException
from src.domain.exceptions.TeamException import TeamException
from src.domain.exceptions.TeamServerErrorException import TeamServerErrorException
from src.domain.exceptions.TeamNotFoundException import TeamNotFoundException

from src.core.dependencies import get_team_service

team_router = APIRouter()


@team_router.get("/")
async def get_teams(service: TeamService = Depends(get_team_service)):
    try:
        teams = await service.get_teams()
        return teams
    except TeamNotFoundException as e:
        raise HTTPException(status_code=404, detail=(e.detail))
    except TeamServerErrorException as e:
        raise HTTPException(status_code=500, detail=(e.detail))
    except TeamException as e:
        raise HTTPException(status_code=400, detail=(e.detail))


@team_router.get("/{team_id}")
async def get_team_by_id(team_id: str, service: TeamService = Depends(get_team_service)):
    try:
        team = await service.get_team_by_id(team_id)
        return team
    except TeamNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.detail)
    except TeamServerErrorException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    except TeamBadRequestException as e:
        raise HTTPException(status_code=400, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
