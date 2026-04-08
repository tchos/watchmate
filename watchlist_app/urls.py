from django.urls import path
from .views import MovieListView, MovieDetailView

app_name = 'watchlist'

urlpatterns = [
    path("list/", MovieListView.as_view(), name="movie-list"),
    path("detail/<int:pk>", MovieListView.as_view(), name="movie-list"),
]