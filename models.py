from pydantic import BaseModel, Field

class LeituraSensores(BaseModel):
    cultura: str = Field(..., description="Nome da planta cultivada, ex: Alface Crespa")
    ph: float = Field(..., description="Nível de pH da água")
    temperatura: float = Field(..., description="Temperatura da água em graus Celsius")
    umidade: float = Field(..., description="Umidade relativa do ar em porcentagem")