from typing import Dict
from app.repositories.orixa_repository import OrixaRepository
from app.schemas.cabala_schema import CabalaResponse, OrixaResponse
from fastapi import HTTPException

class CalcularCabalaUseCase:
    def __init__(self, orixa_repository: OrixaRepository):
        self.orixa_repository = orixa_repository

    def _reduce_to_single_digit(self, num: int) -> int:
        while num > 16:
            num = sum(int(digit) for digit in str(num))
        return num

    def _get_orixa_response(self, numero: int) -> OrixaResponse:
        orixa = self.orixa_repository.get_by_id(numero)
        return OrixaResponse(
            numero=numero,
            orixa=orixa.name if orixa else "Não encontrado"
        )

    async def execute(self, data: str) -> CabalaResponse:
        try:
            # Aceita tanto formato DD/MM/AAAA quanto DD-MM-AAAA
            if '-' in data:
                dia, mes, ano = map(int, data.split('-'))
            else:
                dia, mes, ano = map(int, data.split('/'))
            
            # Validação básica da data
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1000 <= ano <= 9999):
                raise HTTPException(status_code=400, detail="Data inválida. Use o formato DD/MM/AAAA ou DD-MM-AAAA")
                
            # Extrai os dígitos de dia, mês e ano
            n1, n2 = divmod(dia, 10)
            n3, n4 = divmod(mes, 10)
            n5 = ano // 1000
            n6 = (ano % 1000) // 100
            n7 = (ano % 100) // 10
            n8 = ano % 10

            # Calcula somas e reduz para valores de 1 a 16
            soma1 = self._reduce_to_single_digit(n1 + n3 + n5 + n7)
            soma2 = self._reduce_to_single_digit(n2 + n4 + n6 + n8)

            dinheiro = soma1
            pessoas = soma2

            # Calcula o valor do Coração, Racional, Destino e Fé
            soma_coracao = self._reduce_to_single_digit(soma1 + soma2)
            coracao = soma_coracao

            soma_racional = self._reduce_to_single_digit(soma1 + soma2 + soma_coracao)
            racional = soma_racional

            soma_destino = self._reduce_to_single_digit(soma1 + soma2 + soma_coracao + soma_racional)
            destino = soma_destino

            soma_fe = self._reduce_to_single_digit(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8)
            fe = soma_fe

            return CabalaResponse(
                data=f"{dia:02d}/{mes:02d}/{ano}",
                dinheiro=self._get_orixa_response(dinheiro),
                pessoas=self._get_orixa_response(pessoas),
                coracao=self._get_orixa_response(coracao),
                racional=self._get_orixa_response(racional),
                destino=self._get_orixa_response(destino),
                fe=self._get_orixa_response(fe)
            )
        except ValueError:
            raise HTTPException(status_code=400, detail="Formato de data inválido. Use DD/MM/AAAA ou DD-MM-AAAA") 