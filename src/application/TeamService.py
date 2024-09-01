from src.domain.exceptions.TeamBadRequestException import TeamBadRequestException
from src.infraestructure.outbound.externalClients.TeamClient import TeamClient
from src.domain.exceptions.TeamNotFoundException import TeamNotFoundException
from src.domain.exceptions.TeamServerErrorException import TeamServerErrorException
from src.domain.exceptions.TeamException import TeamException


class TeamService:

    def __init__(self, client: TeamClient):
        self.client = client

    async def get_teams(self):
        try:
            teams = await self.client.get_teams()
            return teams
        except TeamNotFoundException as e:
            raise e
        except TeamServerErrorException as e:
            raise e
        except Exception as e:
            raise TeamException("An unknown error occurred") from e

    async def get_team_by_id(self, team_id: str):
        try:
            team = await self.client.get_team_by_id(team_id)
            return team
        except TeamNotFoundException as e:
            raise e
        except TeamServerErrorException as e:
            raise e
        except TeamBadRequestException as e:
            raise e
        except Exception as e:
            raise TeamException(team_id) from e
