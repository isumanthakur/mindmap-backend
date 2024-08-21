from django.urls import path
from .views import MoodInsightsView

urlpatterns = [
    path('', MoodInsightsView.as_view(), name='mood-insights'),
]
