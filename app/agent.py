from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import tmdb_api
from settings import OPENAI_API_KEY

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
parser = StrOutputParser()

template_message = ChatPromptTemplate.from_messages([
    ("system", "Responda apenas com informações disponíveis na API do TMDB. Não dê opiniões pessoais nem discuta temas sensíveis."),
    ("human", "{pergunta}")
])

chain = template_message | model | parser

def format_response(question, data):
    if "elenco" in question.lower():
        elenco = [member['name'] for member in data]
        return f"O elenco principal do filme inclui: {', '.join(elenco[:5])}." if elenco else "Elenco não encontrado."

    elif "sinopse" in question.lower():
        sinopse = data.get('overview', 'Sinopse não disponível.')
        return f"A sinopse do filme é: {sinopse}"

    elif "avaliação" in question.lower():
        rating = data.get('vote_average')
        return f"O filme tem uma avaliação média de {rating}." if rating else "Avaliação não disponível."

    elif "populares" in question.lower():
        filmes_populares = [movie['title'] for movie in data.get('results', [])]
        return f"Filmes populares no momento incluem: {', '.join(filmes_populares[:5])}." if filmes_populares else "Nenhum filme popular encontrado."

    elif "similar" in question.lower():
        filmes_similares = [movie['title'] for movie in data]
        return f"Filmes similares incluem: {', '.join(filmes_similares[:5])}." if filmes_similares else "Nenhum filme similar encontrado."


    elif "recomendação" in question.lower():
        filmes_recomendados = [movie['title'] for movie in data.get('results', [])]
        return f"Recomendações de filmes: {', '.join(filmes_recomendados[:5])}." if filmes_recomendados else "Nenhuma recomendação disponível."

    return "Não consegui entender sua pergunta. Por favor, tente reformulá-la."

def generate_response(question):
    if "elenco" in question.lower():
        movie = tmdb_api.search_movie(question.split("‘")[1].split("’")[0])
        if movie['results']:
            movie_id = movie['results'][0]['id']
            data = tmdb_api.get_movie_cast(movie_id)
            return format_response(question, data)

    elif "sinopse" in question.lower() or "avaliação" in question.lower():
        movie = tmdb_api.search_movie(question.split("‘")[1].split("’")[0])
        if movie['results']:
            movie_id = movie['results'][0]['id']
            data = tmdb_api.get_movie_details(movie_id)
            return format_response(question, data)

    elif "populares" in question.lower():
        data = tmdb_api.get_popular_movies()
        return format_response(question, data)

    elif "similar" in question.lower():
        movie = tmdb_api.search_movie(question.split("‘")[1].split("’")[0])
        if movie['results']:
            movie_id = movie['results'][0]['id']
            data = tmdb_api.get_similar_movies(movie_id)
            return format_response(question, data)

    elif "recomendação" in question.lower():
        genre = question.split("‘")[1].split("’")[0]
        data = tmdb_api.get_top_rated_movies()
        return format_response(question, data)

    return "Não consegui encontrar uma resposta para sua pergunta."
