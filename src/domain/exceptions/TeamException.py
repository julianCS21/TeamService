class TeamException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.detail = f"Team error: {name}"