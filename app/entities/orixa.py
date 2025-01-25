from dataclasses import dataclass

@dataclass
class Orixa:
    id: int
    name: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        } 