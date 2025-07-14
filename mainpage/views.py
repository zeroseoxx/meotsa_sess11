from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Movie

def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(movies, 12)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    # 페이지 번호 범위
    left_index = max(int(page) - 2, 1)
    right_index = min(int(page) + 2, paginator.num_pages)
    custom_range = range(left_index, right_index + 1)

    context = {
        'page_obj': page_obj,
        'query': query,
        'custom_range': custom_range,
    }

    return render(request, 'movies/movie_list.html', context)
