from src.domain.exceptions.TeamException import TeamException


class TeamBadRequestException(TeamException):
    def __init__(self):
        super().__init__("Bad request")
        self.detail = "This request is not valid"