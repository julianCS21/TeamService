from pydantic import BaseModel
from typing import List, Optional


class Competition(BaseModel):
    id: int
    name: str
    code: str
    type: str
    emblem: Optional[str]