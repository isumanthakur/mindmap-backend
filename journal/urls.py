# journal/urls.py
from django.urls import path
from .views import JournalListCreateView, JournalRetrieveUpdateDestroyView

urlpatterns = [
    path('', JournalListCreateView.as_view(), name='journal-list-create'),
    path('<int:pk>/', JournalRetrieveUpdateDestroyView.as_view(), name='journal-detail'),
]
