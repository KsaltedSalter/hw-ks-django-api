from django.shortcuts import render
from django.http import HttpResponse

from barbiemovies.models import BarbieMovies

# Create your views here.
def index(request):
    list = BarbieMovies.objects.all()
    context = {'babrbiemovies': list}
    return render(request, 'barbiemovies/index.html', context)