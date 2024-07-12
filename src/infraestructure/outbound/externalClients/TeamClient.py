import httpx
from src.core.config import Settings
from src.domain.exceptions.TeamException import  TeamException
from src.domain.exceptions.TeamServerErrorException import  TeamServerErrorException
from src.domain.exceptions.TeamNotFoundException import  TeamNotFoundException


class TeamClient:

    def __init__(self, settings: Settings):
        self.base_url = settings.base_football_url
        self.headers = {
            "X-Auth-Token": settings.api_football_key
        }

    async def get_teams(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/teams", headers=self.headers)
                response.raise_for_status()
                data = response.json()
                return data['teams']
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise TeamNotFoundException()
            else:
                raise TeamServerErrorException()

    async def get_team_by_id(self, team_id: str):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/teams/{team_id}", headers=self.headers)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise TeamNotFoundException()
            else:
                raise TeamServerErrorException()
        except Exception as e:

            raise TeamException(str(team_id)) from e
