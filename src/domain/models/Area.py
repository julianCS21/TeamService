from pydantic import BaseModel
from typing import List, Optional


class Area(BaseModel):
    id: int
    name: str
    code: str
    flag: Optional[str]
