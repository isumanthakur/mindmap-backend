from django.urls import path
from .views import MoodListCreateView, MoodRetrieveUpdateDestroyView, MoodSuggestionsView, SpotifySongsView

urlpatterns = [
    path('', MoodListCreateView.as_view(), name='mood-list-create'),
    path('<int:pk>/', MoodRetrieveUpdateDestroyView.as_view(), name='mood-detail'),
    path('suggestions/', MoodSuggestionsView.as_view(), name='mood-suggestions'),
    path('spotify/songs/', SpotifySongsView.as_view(), name='spotify-songs'),  # Add this line
]
