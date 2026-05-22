import os
from dotenv import load_dotenv

load_dotenv()

# Recupera a chave e já aplica o padrão "Fail Fast"
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    # Comentário de intenção: Justifica a interrupção abrupta do sistema.
    # Sem a chave, não há motivo para subir o servidor, pois todas as rotas falhariam.
    raise RuntimeError("GEMINI_API_KEY ausente. Verifique o arquivo .env.")