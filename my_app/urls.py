from django.urls import path, include
from .views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # alias name 即使改变了url别名也可以在html中起作用
    path('movieapp/', include('movies.urls')),
    path('linkapp/', include('links.urls')),
    path('linkplantapp/', include('link_plant.urls')),
    path('trip/', include('trip.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
