from django.conf import settings
from django.db import models

class Mood(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('anxious', 'Anxious'),
        ('neutral', 'Neutral'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)  # Corrected maxLength to max_length
    date = models.DateTimeField(auto_now_add=True)  # Updated to DateTimeField

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.date}"
