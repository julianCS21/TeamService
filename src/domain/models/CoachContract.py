from pydantic import BaseModel
from typing import List, Optional


class CoachContract(BaseModel):
    start: Optional[str]
    until: Optional[str]