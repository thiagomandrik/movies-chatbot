from tmdb_api import search_movie, get_movie_details, get_popular_movies, get_top_rated_movies
import requests

def get_movie_cast_synopsis_rating(name):
    movie = search_movie(name).get('results', [])[0]
    movie_details = get_movie_details(movie['id'])
    cast = ", ".join([cast_member['name'] for cast_member in movie_details.get('credits', {}).get('cast', [])[:5]])
    synopsis = movie_details.get('overview', 'Sinopse indisponível.')
    rating = movie_details.get('vote_average', 'Avaliação indisponível')
    return f"O elenco é: {cast}. A sinopse: {synopsis}. Avaliação: {rating}/10."

def get_popular_movies_response():
    popular_movies = get_popular_movies().get('results', [])
    return "Os filmes populares no momento são: " + ", ".join([movie['title'] for movie in popular_movies[:5]])

def recommend_movie_by_genre(genre_name):
    top_movies = get_top_rated_movies().get('results', [])
    filtered_movies = [movie for movie in top_movies if genre_name in [genre['name'] for genre in movie['genres']]]
    if filtered_movies:
        return f"Baseado no gênero '{genre_name}', eu recomendo '{filtered_movies[0]['title']}'!"
    return f"Não encontrei nenhum filme top no gênero {genre_name}."

def get_similar_movie(name):
    movie = search_movie(name).get('results', [])[0]
    similar_movies_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/similar"
    params = {
        "api_key": "sua_chave_da_api",
        "language": "pt-BR"
    }
    response = requests.get(similar_movies_url, params=params).json()
    similar_movies = response.get('results', [])
    if similar_movies:
        return f"Um filme similar ao '{name}' é '{similar_movies[0]['title']}'."
    return f"Não encontrei filmes similares a '{name}'."
