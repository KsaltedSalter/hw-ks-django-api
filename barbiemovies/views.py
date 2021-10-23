from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import serializers, views, response, status, exceptions

from barbiemovies.models import BarbieMovie
from .serializers import BarbieMovieSerializer

# Create your views here.
def index(request):
    list = BarbieMovie.objects.all()
    context = {'babrbiemovies': list}
    return render(request, 'barbiemovies/index.html', context)

class BarbieMoviesListView(views.APIView):
    def get(self, request):
        barbiemovies = BarbieMovie.objects.all()
        serialized_barbiemovies = BarbieMovieSerializer(barbiemovies, many=True)
        return response.Response(serialized_barbiemovies.data, status=status.HTTP_200_OK )

    def post(self, request):
        print(request.data)
        barbiemovie_to_add = BarbieMovieSerializer(data=request.data)
        if barbiemovie_to_add.is_valid():
            barbiemovie_to_add.save()
            return response.Response(barbiemovie_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(barbiemovie_to_add.errors, status=status.HTTP_400_BAD_REQUEST)

class BarbieMovieDetailView(views.APIView):
    def get_barbiemovie_by_id(self, id):
        try:
            return BarbieMovie.objects.get(id=id)
        except BarbieMovie.DoesNotExist:
            raise exceptions.NotFound(detail="Oh dear! This movie is not part of the Babrie catalogue")

    def get(self, request, id):
        barbiemovie = self.get_barbiemovie_by_id(id)
        serialized_barbiemovie = BarbieMovieSerializer(barbiemovie)
        return response.Response(serialized_barbiemovie.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        barbiemovie = self.get_barbiemovie_by_id(id)
        barbiemovie.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        barbiemovie = self.get_barbiemovie_by_id(id)
        updated_barbiemovie = BarbieMovieSerializer(barbiemovie, data=request.data)
        if updated_barbiemovie.is_valid():
            updated_barbiemovie.save()
            return response.Response(updated_barbiemovie.data, status=status.HTTP_201_CREATED)
        return response.Response(updated_barbiemovie.errors, status=status.HTTP_400_BAD_REQUEST) 