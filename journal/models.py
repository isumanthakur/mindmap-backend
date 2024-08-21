# journal/models.py
from django.conf import settings
from django.db import models

class Journal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='journal_images/', blank=True, null=True)
    video = models.FileField(upload_to='journal_videos/', blank=True, null=True)
    voice_note = models.FileField(upload_to='journal_voice_notes/', blank=True, null=True)
    gif = models.ImageField(upload_to='journal_gifs/', blank=True, null=True)

    def __str__(self):
        return f"Journal entry by {self.user.username} at {self.created_at}"
