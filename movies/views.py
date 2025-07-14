import requests
from django.http import JsonResponse
from .models import Movie, Actor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework import status

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


def init_db(request):
    url = "http://43.200.28.219:1313/movies/"
    res = requests.get(url)

    if res.status_code != 200:
        return JsonResponse({'error': '데이터를 불러오는 데 실패했습니다'}, status=500)
    
    movies_data = res.json()['movies']

    for m in movies_data:
        movie = Movie.objects.create(
            title_kor=m['title_kor'],
            title_eng=m['title_eng'],
            poster_url=m['poster_url'],
            genre=m['genre'],
            showtime=m['showtime'],
            release_date=m['release_date'],
            plot=m['plot'],
            audience_score=m['rating'],
            director_name=m['director_name'],
            director_image_url=m['director_image_url'],
        )

        for actor in m['actors']:
            Actor.objects.create(
                movie=movie,
                name=actor['name'],
                character=actor['character'],
                image_url=actor['image_url'],
            )

    return JsonResponse({'message': '영화 데이터 저장 완료'})

