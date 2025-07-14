from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Movie
import requests
from django.http import HttpResponse


# api에서 영화 데이터 가져옴
def fetch_movies_from_api():
    url = "http://43.200.28.219:1313/movies/"
    response = requests.get(url)
    movies_data = response.json().get('movies', [])
    return movies_data

def movie_list(request):
    movies = fetch_movies_from_api()
    return render(request, 'movies/movie_list.html', {'movies': movies})



# 제목, 포스터 띄움
def init_db(request):
    movies = fetch_movies_from_api()
    for item in movies:
        Movie.objects.create(
            title_kor=item['title_kor'],
            poster_url=item['poster_url']
        )
    return HttpResponse("DB 초기화 완료!")



# 영화 검색창
def movie_list(request):
    query = request.GET.get('q')  
    if query:
        movies = Movie.objects.filter(title__icontains=query)  
    else:
        movies = Movie.objects.all()

    paginator = Paginator(movies, 12)
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)


    left_index = max(int(page or 1) - 2, 1)
    right_index = min(int(page or 1) + 2, paginator.num_pages)
    custom_range = range(left_index, right_index + 1)

    context = {
        'page_obj': page_obj,
        'custom_range': custom_range,
        'query': query,  
    }
    return render(request, 'movies/movie_list.html', context)

