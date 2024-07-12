from pydantic import BaseModel
from typing import List, Optional

from src.domain.models.CoachContract import CoachContract


class Coach(BaseModel):
    id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    name: Optional[str]
    dateOfBirth: Optional[str]
    nationality: Optional[str]
    contract: Optional[CoachContract]