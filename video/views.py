from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Video
from django.urls import reverse_lazy

def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'video/home.html', context)


class VideoListView(ListView):
    model = Video
    template_name = 'video/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'videos'
    ordering = ['-date_posted']


class VideoDetailView(DetailView):
    model = Video


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'content', 'video_url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'content', 'video_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False
