from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import MovieSerializer, MovieMiniSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)