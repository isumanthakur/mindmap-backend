from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mood
from .serializers import MoodSerializer
from .spotify_utils import get_songs_for_mood

class MoodListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the mood entry
        serializer.save(user=self.request.user)

class MoodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user)

class MoodSuggestionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        mood = Mood.objects.filter(user=request.user).latest('date').mood
        # Provide a default suggestion or handle without GPT
        suggestions = "Here are some default suggestions based on your mood."
        songs = get_songs_for_mood(mood)
        return Response({'mood': mood, 'suggestions': suggestions, 'songs': songs})

class SpotifySongsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mood = request.query_params.get('mood', 'neutral')
        songs = get_songs_for_mood(mood)
        return Response(songs)
