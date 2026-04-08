from django.shortcuts import render
from watchlist_app.models import Movie
from django.views.generic import ListView, DetailView

# Create your views here.
class MovieListView(ListView):
    # Le modele pour lequel nous voulons lister le contenu
    model = Movie

class MovieDetailView(DetailView):
    # Le modele pour lequel nous voulons lister le contenu
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context