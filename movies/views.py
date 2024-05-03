from django.shortcuts import render, HttpResponse
import datetime


def index(request):
    movie_list = [
        '星球大战：新希望',
        '银河护卫队',
    ]
    content = {
        'date_today': datetime.date.today(),
        'movies': movie_list,
    }
    return render(request, 'movies/index.html', content)


def about(request):
    return render(request, 'movies/about.html', {})
