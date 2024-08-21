from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import get_mood_insights

class MoodInsightsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        insights = get_mood_insights(request.user)
        return Response(insights)
