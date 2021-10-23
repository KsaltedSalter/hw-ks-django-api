from django.urls import path
from .views import BarbieMovieDetailView, BarbieMoviesListView, index 

urlpatterns = [
    path("", index),
    path("api/", BarbieMoviesListView.as_view()),
    path("api/<int:id>/", BarbieMovieDetailView.as_view()),
]