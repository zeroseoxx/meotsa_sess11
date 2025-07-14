from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieDetailSerializer
from .serializers import CommentCreateSerializer, CommentResponseSerializer
from movies.models import Movie
from .models import Comment


#영화 세부 정보 보여주기 (1개의 영화정보/ 코멘트까지 함께 )
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

#영화 코멘트 작성 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({"error": "영화를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.save(user=request.user, movie=movie)
        response_serializer = CommentResponseSerializer(comment)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#평점 작성 
