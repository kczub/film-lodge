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

def get_film_credits(api_key, movie_id):
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f'{base_url}/movie/{movie_id}/credits?api_key={api_key}'
    
    r = requests.get(endpoint)
    # if r.status_code != r.ok:
    #     # print(r.status_code)
    #     return None
        
    results = r.json()
    cast = results.get('cast')
    crew = results.get('crew')
    film_credits = {
        'cast': [x['name'] for x in cast][:11],
        'director': next((x['name'] for x in crew if x['job'] == 'Director'), None),
        'screenplay': next((x['name'] for x in crew if x['job'] == 'Writer'), None),
        'dop': next((x['name'] for x in crew if x['job'] == 'Director of Photography'), None),
    }
    return film_credits

def get_film_details(api_key, movie_id):
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f'{base_url}/movie/{movie_id}?api_key={api_key}'
    
    r = requests.get(endpoint)
    # if r.status_code != r.ok:
    #     return None
    
    results = r.json()
    film_details = {
        'title': results.get('title'),
        'overview': results.get('overview'),
        'release_date': results.get('release_date')
    }

    return film_details
