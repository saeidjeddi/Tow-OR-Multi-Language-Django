from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG

from home.views import ChangLang

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('lang', ChangLang.as_view(), name='langs')
]

urlpatterns += i18n_patterns(
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)