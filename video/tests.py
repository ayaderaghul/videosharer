from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from .models import Video

class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(first_name='Lana', last_name='Jeans')
        v = Video.objects.create(title='Hello world', 
            content='Hello world content', video_url='youtube.com/abc', 
            author=u)
        self.assertEqual(v.title, 'Hello world')
        self.assertEqual(v.author, u)


