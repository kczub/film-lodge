from django.urls import path

from .views import index_view, search_view, film_details_view


app_name = 'films'
urlpatterns = [
    path('', index_view, name='index'),
    path('search/', search_view, name='search'),
    path('<int:movie_id>/details/', film_details_view, name='details')
]