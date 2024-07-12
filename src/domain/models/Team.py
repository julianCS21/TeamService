from pydantic import BaseModel
from typing import List, Optional

from src.domain.models.Area import Area
from src.domain.models.Competition import Competition
from src.domain.models.Coach import Coach
from src.domain.models.SquadMember import SquadMember


class Team(BaseModel):
    area: Area
    id: int
    name: str
    shortName: str
    tla: str
    crest: Optional[str]
    address: str
    website: str
    founded: int
    clubColors: str
    venue: str
    runningCompetitions: List[Competition]
    coach: Optional[Coach]
    squad: List[SquadMember]
    staff: List[str]
    lastUpdated: str
