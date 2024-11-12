import pytest
import httpx
from fastapi import status

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_elenco_do_filme():
    question = "Qual é o elenco do filme ‘Matrix’?"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/chat", json={"question": question})
        print(f'{question}\n')
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert "O elenco principal do filme inclui:" in data["answer"]
        print(f"{data['answer']} \n\n")

@pytest.mark.asyncio
async def test_sinopse_do_filme():
    question = "Qual é a sinopse do filme ‘Matrix’?"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/chat", json={"question": question})
        print(f'{question}\n')
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert "A sinopse do filme é:" in data["answer"]
        print(f"{data['answer']} \n\n")

@pytest.mark.asyncio
async def test_avaliacao_do_filme():
    question = "Qual é a avaliação do filme ‘Inception’?"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/chat", json={"question": question})
        print(f'{question}\n')
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert "O filme tem uma avaliação média de" in data["answer"]
        print(f"{data['answer']}\n\n")

@pytest.mark.asyncio
async def test_filmes_populares():
    question = "Quais são os filmes populares no momento?"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/chat", json={"question": question})
        print(f'{question}\n')
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert "Filmes populares no momento incluem:" in data["answer"]
        print(f"{data['answer']} \n\n")

@pytest.mark.asyncio
async def test_filmes_similares():
    question = "Quero um filme similar ao ‘Matrix’"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/chat", json={"question": question})
        print(f'{question}\n')
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert "answer" in data
        assert isinstance(data["answer"], str)
        assert "Filmes similares incluem:" in data["answer"]
        print(f"{data['answer']} \n\n")
