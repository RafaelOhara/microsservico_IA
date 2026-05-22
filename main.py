import json
from fastapi import FastAPI, HTTPException
from models import LeituraSensores
from ia_service import analisar_dados_cultivo

app = FastAPI(title="Microserviço IA - Hidroponia")

@app.post("/analisar-cultivo")
async def analisar_cultivo(dados: LeituraSensores):
    try:
        resultado = analisar_dados_cultivo(dados)
        return resultado

    except json.JSONDecodeError:
        # Erros 500 indicam falha no servidor (neste caso, a IA devolveu algo ilegível).
        raise HTTPException(
            status_code=500, 
            detail="O serviço de inteligência artificial não retornou dados processáveis."
        )
    except Exception as erro_inesperado:
        raise HTTPException(
            status_code=500, 
            detail=f"Falha interna ao processar análise: {str(erro_inesperado)}"
        )