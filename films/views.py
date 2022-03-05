from django.shortcuts import render
from django.conf import settings

from .connect import search_movie

api_key = settings.API_KEY

def index_view(request):
    search_query = request.GET['q']
    search_results = search_movie(api_key=api_key, query=search_query)
    results = search_results['results']
    context = {
        'object_list': results
    }
    return render(request, 'films/index.html', context)
