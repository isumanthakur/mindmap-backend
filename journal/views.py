# journal/views.py
from rest_framework import generics, permissions
from .models import Journal
from .serializers import JournalSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class JournalListCreateView(generics.ListCreateAPIView):
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JournalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)
