from typing import List, Optional
from app.entities.orixa import Orixa

class OrixaRepository:
    def __init__(self):
        self.orixas = [
            Orixa(id=1, name="Exu"),
            Orixa(id=2, name="Ibeji"),
            Orixa(id=3, name="Ogum"),
            Orixa(id=4, name="Omolu"),
            Orixa(id=5, name="Oxum"),
            Orixa(id=6, name="Obará"),
            Orixa(id=7, name="Obaluaê"),
            Orixa(id=8, name="Ejionilê"),
            Orixa(id=9, name="Iemanjá"),
            Orixa(id=10, name="Oxalufá"),
            Orixa(id=11, name="Owonrin"),
            Orixa(id=12, name="Xangô"),
            Orixa(id=13, name="Nanã"),
            Orixa(id=14, name="Oxumaré"),
            Orixa(id=15, name="Obá"),
            Orixa(id=16, name="Oxalá")
        ]

    def get_by_id(self, id: int) -> Optional[Orixa]:
        for orixa in self.orixas:
            if orixa.id == id:
                return orixa
        return None

    def get_all(self) -> List[Orixa]:
        return self.orixas 