# tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Journal

class JournalTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.journal = Journal.objects.create(
            user=self.user,
            content='This is a test journal entry.'
        )

    def test_journal_creation(self):
        self.assertEqual(self.journal.user.username, 'testuser')
        self.assertEqual(self.journal.content, 'This is a test journal entry.')
