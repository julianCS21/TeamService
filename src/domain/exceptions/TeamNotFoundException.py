from src.domain.exceptions.TeamException import TeamException


class TeamNotFoundException(TeamException):
    def __init__(self):
        super().__init__("Team not found")
        self.detail = "The requested team was not found."