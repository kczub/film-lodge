from django.shortcuts import render
from django.conf import settings

from .connect import search_movie, get_film_credits, get_film_details

api_key = settings.API_KEY

def index_view(request):
    context = {}
    return render(request, 'films/index.html', context)


def search_view(request):
    # print(request.GET)
    search_query = request.GET['q']
    search_results = search_movie(api_key=api_key, query=search_query)
    results = [x for x in search_results['results']]
    context = {
        'object_list': results
    }
    return render(request, 'films/search_results.html', context)


def film_details_view(request, movie_id):
    film_details = get_film_details(api_key, movie_id=movie_id)
    film_credits = get_film_credits(api_key, movie_id=movie_id)
    
    film_details.update(film_credits)
    # print(film_details)
    return render(request, 'films/detail.html', context=film_details)
