from django.db.models import Avg, Count
from moods.models import Mood

MOOD_MAP = {
    'angry': 1,
    'anxious': 2,
    'neutral': 3,
    'happy': 4,
    'sad': 5,
}

def get_mood_insights(user):
    moods = Mood.objects.filter(user=user)
    most_frequent_mood = moods.values('mood').annotate(count=Count('mood')).order_by('-count').first()
    
    # Calculate average mood
    mood_values = moods.values_list('mood', flat=True)
    mood_scores = [MOOD_MAP[mood] for mood in mood_values]
    if mood_scores:
        average_mood = sum(mood_scores) / len(mood_scores)
    else:
        average_mood = 0
    
    return {
        'most_frequent_mood': most_frequent_mood['mood'] if most_frequent_mood else None,
        'average_mood': average_mood
    }
