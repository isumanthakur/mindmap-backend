# tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

class CommunityTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.post = Post.objects.create(
            user=self.user,
            content='This is a test post.'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content='This is a test comment.'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.content, 'This is a test post.')

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.user.username, 'testuser')
        self.assertEqual(self.comment.content, 'This is a test comment.')
