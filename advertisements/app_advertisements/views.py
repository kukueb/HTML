from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm
# Create your views here.

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisements(request):
    return render(request, 'advertisement.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form':form} 
    return render(request, 'advertisement-post.html', context)
            

