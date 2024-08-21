from django.conf import settings
from django.db import models

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=255)
    target = models.IntegerField()
    progress = models.IntegerField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.goal_type}"
