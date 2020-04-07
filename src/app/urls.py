from django.urls import path
from .views import home, new_search

app_name = 'app'

urlpatterns = [
    path('', home, name='home-page'),
    path('new_search/', new_search, name='new-search-page'),
]