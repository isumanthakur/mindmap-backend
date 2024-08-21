from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'user', 'goal_type', 'target', 'progress', 'start_date', 'end_date']
        read_only_fields = ['id', 'user', 'start_date']
