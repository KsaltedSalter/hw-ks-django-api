from rest_framework import serializers

from barbiemovies.models import BarbieMovie

class BarbieMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarbieMovie
        fields = '__all__'