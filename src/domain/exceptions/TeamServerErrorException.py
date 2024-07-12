from src.domain.exceptions.TeamException import TeamException


class TeamServerErrorException(TeamException):
    def __init__(self):
        super().__init__("Server error")
        self.detail = "A server error occurred while processing the team."
