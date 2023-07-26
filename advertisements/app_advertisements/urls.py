from django.urls import path
from .views import index, top_sellers, advertisements, advertisement_post, login, profile, register

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisements/', advertisements, name='advertisements'),
    path('advertisements_post/', advertisement_post, name='advertisement-post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]