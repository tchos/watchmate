from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieDetailApiView, MovieListApiView

app_name = 'watchlist'

urlpatterns = [
    path("list/", MovieListApiView.as_view(), name="movie-list"),
    path("detail/<int:pk>", MovieDetailApiView.as_view(), name="movie-list"),
]