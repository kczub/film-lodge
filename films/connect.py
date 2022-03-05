from django.conf import settings
import requests


api_key = settings.API_KEY

def search_movie(api_key, query):
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f'{base_url}/search/movie?api_key={api_key}&query={query}'

    r = requests.get(endpoint)
    if r.status_code != r.ok:
        print(r.status_code)
        
    results = r.json()
    return results