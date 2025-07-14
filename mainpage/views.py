from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.
def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    
    paginator = Paginator(movies, 12)  # 12개씩 보여주기
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/movie_list.html', {'page_obj': page_obj})



def post_list(request):
    post_list = Movie.objects.all()
    page = request.GET.get('page')


    paginator = Paginator(post_list, 2)


    try: 
        page_obj = paginator.page(page) 

    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 2)
    if leftIndex > paginator.num_pages:
        rightIndex = paginator.num_pages


    custom_range = range(leftIndex, rightIndex+1)
    return render(request, 'post/post_list_html', {'post_list':post_list, 'page_obj':page_obj})
# post html은 영화 데이터 받고 나서 수정