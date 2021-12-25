from django.shortcuts import render

videos = [
    {
        'author': 'chi',
        'title': 'video 1',
        'content': 'first video content',
        'date_posted': 'Dec 25, 2021'
    },
    {
        'author': 'jane',
        'title': 'video 2',
        'content': 'second video content',
        'date_posted': 'Jan 2, 2022'
    }
]

def home(request):
    context = {
        'videos': videos
    }
    return render(request, 'video/home.html', context)

