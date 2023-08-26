from django.urls import path
from .views import index, top_sellers, advertisements, advertisement_post, login, profile, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisements/', advertisements, name='advertisements'),
    path('advertisements-post/', advertisement_post, name='advertisement-post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)