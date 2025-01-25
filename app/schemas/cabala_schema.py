from pydantic import BaseModel, Field
from datetime import date
from typing import Dict

class CabalaRequest(BaseModel):
    data: str = Field(..., description="Data no formato DD/MM/AAAA ou DD-MM-AAAA")

class OrixaResponse(BaseModel):
    numero: int
    orixa: str

class CabalaResponse(BaseModel):
    data: str
    dinheiro: OrixaResponse
    pessoas: OrixaResponse
    coracao: OrixaResponse
    racional: OrixaResponse
    destino: OrixaResponse
    fe: OrixaResponse 