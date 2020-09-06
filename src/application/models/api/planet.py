from pydantic import BaseModel
from typing import Optional


class Planet(BaseModel):
    id: Optional[str] = None
    name: str
    climate: str
    terrain: str
    apparition_counter: Optional[int] = None

    def to_mongo_dict(self) -> dict:
        return {
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
        }

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "apparition_counter": self.apparition_counter
        }
