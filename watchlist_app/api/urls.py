from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListApiView, WatchListDetailApiView, StreamPlatformListApiView, StreamPlatformDetailApiView, ReviewList, ReviewDetail

app_name = 'watchlist'

urlpatterns = [
    path("list", WatchListApiView.as_view(), name="movie-list"),
    path("detail/<int:pk>", WatchListDetailApiView.as_view(), name="movie-detail"),
    path("stream", StreamPlatformListApiView.as_view(), name="stream-list"),
    path("stream/<int:pk>", StreamPlatformDetailApiView.as_view(), name="stream-detail"),
    path("review", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]