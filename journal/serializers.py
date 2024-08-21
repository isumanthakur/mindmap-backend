# journal/serializers.py
from rest_framework import serializers
from .models import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'user', 'content', 'created_at', 'image', 'video', 'voice_note', 'gif']
        read_only_fields = ['id', 'user', 'created_at']
