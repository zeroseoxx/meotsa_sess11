from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieDetailSerializer
from movies.models import Movie
from .models import Comment


#영화 세부 정보 보여주기 (1개의 영화정보/ 코멘트까지 함께 )
@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

#영화 코멘트 조회 (여러 개의 코멘트)
@api_view(['GET'])
def moive_comment(request):
    comments = Comment


#영화 코멘트 작성 


#평점 작성 
