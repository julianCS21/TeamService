from pydantic import BaseModel
from typing import List, Optional


class SquadMember(BaseModel):
    id: int
    name: str
    position: str
    dateOfBirth: str
    nationality: str