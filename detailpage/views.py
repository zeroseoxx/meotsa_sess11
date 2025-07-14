import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

API_URL = "http://43.200.28.219:1313/movies/"

# 영화 전체 목록 가져오기
@api_view(['GET'])
def movie_list(request):
    response = requests.get(API_URL)
    if response.status_code != 200:
        return Response({"error": "영화 데이터를 가져오지 못했습니다."}, status=500)

    movies = response.json().get('movies', [])
    return Response(movies)

# 영화 상세 정보 가져오기
@api_view(['GET'])
def movie_detail(request, movie_id):
    response = requests.get(API_URL)
    if response.status_code != 200:
        return Response({"error": "영화 데이터를 가져오지 못했습니다."}, status=500)

    movies = response.json().get('movies', [])
    try:
        movie = movies[movie_id - 1]  # 주의: movie_id는 1부터 시작한다고 가정
    except IndexError:
        return Response({"error": "해당 영화가 존재하지 않습니다."}, status=404)

    return Response(movie)
