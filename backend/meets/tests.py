from django.test import TestCase
from django.contrib.auth.models import User

from .models import Meet, Comment


# Create your tests here.
class TumitTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='abc')
        testuser1.save()

        test_meet = Meet.objects.create(author=testuser1, title='Blog title',
                                        body='message', likes=10)
        test_meet.save()
        test_comment = Comment.objects.create(author=testuser1, post = test_meet,
                                              comment='home', likes=45)
        test_comment.save()

    def test_meet_data(self):
        meet = Meet.objects.get(id=1)
        author = f'{meet.author}'
        title = f'{meet.title}'
        body = f'{meet.body}'
        likes = f'{meet.likes}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'message')
        self.assertEqual(likes, '10')

    def test_meet_comments(self):
        comment = Comment.objects.get(id=1)
        author = f'{comment.author}'
        post = f'{comment.post}'
        comment_words= f'{comment.comment}'
        likes = f'{comment.likes}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(post,'Blog title')
        self.assertEqual(comment_words, 'home')

