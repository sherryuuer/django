import datetime

from django.shortcuts import render, get_object_or_404
from .models import MoviePosting


def index(request):
    movie_list = MoviePosting.objects.filter(is_active=True)
    context = {
        'date_today': datetime.date.today(),
        'movies': movie_list,
    }
    return render(request, 'movies/index.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(MoviePosting, pk=pk, is_active=True)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


def about(request):
    return render(request, 'movies/about.html', {})
