from fastapi import APIRouter, Depends
from app.schemas.cabala_schema import CabalaResponse
from app.use_cases.calcular_cabala import CalcularCabalaUseCase
from app.repositories.orixa_repository import OrixaRepository

router = APIRouter()

def get_orixa_repository():
    return OrixaRepository()

def get_calcular_cabala_use_case(
    orixa_repository: OrixaRepository = Depends(get_orixa_repository)
) -> CalcularCabalaUseCase:
    return CalcularCabalaUseCase(orixa_repository)

@router.get("/", response_model=dict)
async def root():
    return {"mensagem": "Bem-vindo à API de CABALA em Python!"}

@router.get("/cabala/{data}", response_model=CabalaResponse)
async def calcular_cabala(
    data: str,
    use_case: CalcularCabalaUseCase = Depends(get_calcular_cabala_use_case)
) -> CabalaResponse:
    return await use_case.execute(data) 