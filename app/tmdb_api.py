# tmdb_api.py

import requests
from settings import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"

def search_movie(name):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR", "query": name}
    response = requests.get(url, params=params)
    return response.json()

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params)
    return response.json()

def get_movie_cast(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params)
    return response.json().get("cast", [])

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params)
    return response.json()

def get_top_rated_movies():
    url = f"{BASE_URL}/movie/top_rated"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params)
    return response.json()

def get_similar_movies(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/similar"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params)
    return response.json().get("results", [])
