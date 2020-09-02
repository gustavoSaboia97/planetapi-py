from pydantic import BaseModel
from typing import Optional


class Planet(BaseModel):
    id: Optional[str] = None
    name: str
    climate: str
    terrain: str
    apparition_counter: Optional[int] = None
