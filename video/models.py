from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(default='',max_length=300)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})