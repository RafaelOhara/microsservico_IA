import json
from google import genai
from google.genai import types
from config import API_KEY
from models import LeituraSensores

def _gerar_prompt_agronomico(dados: LeituraSensores) -> str:
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
    4. Se algum valor estiver fora da faixa, o status é "Alerta". Sugira ações corretivas práticas.

    FORMATO DE SAÍDA OBRIGATÓRIO:
    {{
      "parametros_ideais_utilizados": {{"ph": "faixa", "temperatura": "faixa", "umidade": "faixa"}},
      "status_sistema": "Normal ou Alerta",
      "diagnostico_breve": "Resumo rápido",
      "parametros_em_alerta": ["lista de parametros alterados, vazio se Normal"],
      "sugestoes_acao": ["lista de sugestões, vazio se Normal"]
    }}
    """

def _limpar_formatacao_markdown(texto: str) -> str:
    texto = texto.strip()
    if texto.startswith("```"):
        texto = texto.strip("`").replace("json\n", "", 1)
    return texto

def analisar_dados_cultivo(dados: LeituraSensores) -> dict:
    # Checagem de segurança tardia: Se a Azure falhou em ler a chave, a API avisa em vez de quebrar
    if not API_KEY:
        raise ValueError("A chave GEMINI_API_KEY não está configurada no ambiente da Azure.")

    # Inicia o cliente do NOVO SDK
    cliente_ia = genai.Client(api_key=API_KEY)
    prompt = _gerar_prompt_agronomico(dados)
    
    # Chama o modelo usando a nova estrutura do Google
    resposta_bruta = cliente_ia.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    
    texto_limpo = _limpar_formatacao_markdown(resposta_bruta.text)
    return json.loads(texto_limpo)