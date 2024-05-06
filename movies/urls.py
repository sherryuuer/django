from django.urls import path
from .views import index, about, movie_detail

urlpatterns = [
    path('', index, name='movie-home'),  # alias name 即使改变了url别名也可以在html中起作用
    path('about/', about, name='movie-about'),
    path('movie/<int:pk>/', movie_detail, name='movie-detail'),
]
