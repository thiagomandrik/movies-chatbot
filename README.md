# movies-chatbot

O movies-chatbot é um bot desenvolvido em Python que responde perguntas sobre filmes. Desenvolvido usando FastAPI, Lanchain e a API da OpenAI pra processar dados de filmes obtidos via **API TMDB**. 

## Pré-requisitos

- Python 3.10+
- API Key do **TMDB** para acessar informações dos filmes.
- API Key da **OpenAI** para acessar informações dos filmes.

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/movies-chatbot.git
   cd movies-chatbot
   ```

2. Inicie o ambiente virtual e instale as biliotecas necessárias
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Na raiz do projeto, crie o arquivo .env e inclua as variaveis de ambiente necessárias
    ```
    TMDB_API_KEY=''
    OPENAI_API_KEY=''
    ```

4. Inicie o servidor
    ```bash
    python app/main.py
    ```

5. Rodar os testes via PyTest
    ```bash
    pytest app/tests.py -s
    ```

## Testes via curl

1. Testar elenco do filme 'Matrix':
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/chat' \
    -H 'Content-Type: application/json' \
    -d '{"question": "Qual é o elenco do filme ‘Matrix’?"}'

    ```    
2. Testar sinopse do filme 'Matrix':
    ```bash

    curl -X 'POST' \
    'http://localhost:8000/chat' \
    -H 'Content-Type: application/json' \
    -d '{"question": "Qual é a sinopse do filme ‘Matrix`?"}'
    ```

3. Testar avaliação do filme 'Inception':
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/chat' \
    -H 'Content-Type: application/json' \
    -d '{"question": "Qual é a avaliação do filme ‘Matrix’?"}'
    ```

4. Testar filmes populares no momento:
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/chat' \
    -H 'Content-Type: application/json' \
    -d '{"question": "Quais são os filmes populares no momento`?"}'
    ```

5. Testar filmes similares ao 'Matrix':
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/chat' \
    -H 'Content-Type: application/json' \
    -d '{"question": "Quero um filme similar ao ‘Matrix’"}'
    ```