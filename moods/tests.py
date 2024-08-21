# tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Mood

class MoodTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.mood = Mood.objects.create(
            user=self.user,
            mood='happy'
        )

    def test_mood_creation(self):
        self.assertEqual(self.mood.user.username, 'testuser')
        self.assertEqual(self.mood.mood, 'happy')
