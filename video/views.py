from django.shortcuts import render
from .models import Video

def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'video/home.html', context)

