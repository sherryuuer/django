from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),  # alias name 即使改变了url别名也可以在html中起作用
    path('movieapp/', include('movies.urls')),
    path('linkapp/', include('links.urls')),
    path('linkplantapp/', include('link_plant.urls')),
    path('trip/', include('trip.urls')),
    path('menu/', include('menu.urls')),
]
