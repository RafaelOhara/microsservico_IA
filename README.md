# Microserviço IA - Hidroponia Inteligente
# Sobre o Projeto

Este projeto é um microserviço backend desenvolvido em Python (FastAPI) focado em trazer inteligência de dados para sistemas hidropônicos. Ele atua como um sistema de suporte à decisão: recebe dados de telemetria dos sensores do cultivo (pH, temperatura da água e umidade do ar) e, utilizando a API do **Google Gemini (IA Generativa)**, analisa essas condições em tempo real. A IA cruza as leituras com os parâmetros ideais da cultura plantada e devolve um diagnóstico estruturado em JSON, sugerindo ações corretivas imediatas caso o sistema entre em estado de alerta.


# Índice/Sumário

* [Sobre](#sobre-o-projeto)
* [Sumário](#índice/sumário)
* [Requisitos Funcionais](#requisitos-funcionais)
* [Tecnologias Usadas](#tecnologias-usadas)

# Requisitos Funcionais 

- [x] **Receber dados de telemetria via HTTP POST** (cultura, pH, temperatura, umidade)
- [x] **Integração com Google Gemini** (Modelo 2.5 Flash)
- [x] **Geração de Prompt Dinâmico** baseado nos dados recebidos
- [x] **Higienização de Resposta** (Garantia de retorno estrito em JSON)
- [x] **Cobertura de Testes Unitários** (Mocking da IA)
- [ ] Conexão com MQTT (Envio/Recebimento de tópicos IoT)
- [ ] Integração com Banco de Dados para histórico de alertas

# Tecnologias Usadas

- [Python 3](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web para a construção da API
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
- [Google Generative AI](https://aistudio.google.com/) - Integração com o LLM Gemini

# Como Executar

1. Clone o repositório:
   
```bash
   git clone [https://github.com/RafaelOhara/microsservicos_IA.git](https://github.com/RafaelOhara/microsservicos_IA.git)