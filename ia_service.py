import json
import google.generativeai as genai
from config import API_KEY
from models import LeituraSensores

genai.configure(api_key=API_KEY)

MODELO_IA = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={"response_mime_type": "application/json"}
)

def _gerar_prompt_agronomico(dados: LeituraSensores) -> str:
    # O sublinhado no início do nome da função indica que ela é privada (uso interno).
    return f"""
    Você é um agrônomo especialista em hidroponia.

    A cultura atual no sistema é: {dados.cultura}

    Leituras atuais dos sensores:
    - pH da água: {dados.ph}
    - Temperatura da água: {dados.temperatura}°C
    - Umidade do ar: {dados.umidade}%

    Sua tarefa:
    1. Busque no seu próprio conhecimento quais são as faixas ideais de pH, temperatura e umidade para a cultura acima.
    2. Compare as leituras atuais com essas faixas ideais.
    3. Se todos os valores estiverem dentro da faixa, o status é "Normal".
    4. Se algum valor estiver fora, o status é "Alerta". Sugira ações corretivas práticas.

    FORMATO DE SAÍDA OBRIGATÓRIO (APENAS JSON):
    {{
      "parametros_ideais_utilizados": {{"ph": "faixa", "temperatura": "faixa", "umidade": "faixa"}},
      "status_sistema": "Normal ou Alerta",
      "diagnostico_breve": "Resumo rápido",
      "parametros_em_alerta": ["lista de parametros alterados, vazio se Normal"],
      "sugestoes_acao": ["lista de sugestões, vazio se Normal"]
    }}
    """

def _limpar_formatacao_markdown(texto: str) -> str:
    """
    Remove blocos de formatação (```json) que alguns modelos de linguagem
    podem injetar por engano mesmo quando configurados para retornar JSON puro.
    """
    texto = texto.strip()
    if texto.startswith("```"):
        texto = texto.strip("").replace("json\n", "", 1)
    return texto

def analisar_dados_cultivo(dados: LeituraSensores) -> dict:
    prompt = _gerar_prompt_agronomico(dados)
    resposta_bruta = MODELO_IA.generate_content(prompt)
    texto_limpo = _limpar_formatacao_markdown(resposta_bruta.text)
    
    return json.loads(texto_limpo)