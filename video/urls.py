from django.urls import path
from .views import (
    VideoListView, 
    VideoDetailView, 
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView
)
from . import views

urlpatterns = [
    path('', VideoListView.as_view(), name='video-home'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('video/new/', VideoCreateView.as_view(), name='video-create'),
    path('video/<int:pk>/update', VideoUpdateView.as_view(), name='video-update'),
    path('video/<int:pk>/delete', VideoDeleteView.as_view(), name='video-delete'),

]
