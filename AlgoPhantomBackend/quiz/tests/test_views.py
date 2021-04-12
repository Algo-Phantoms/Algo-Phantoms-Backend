from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from quiz.views import QuizQuestion

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='algo', email='algo@gmail.com', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/quetion/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        response = QuizQuestion.as_view()(request)
        self.assertEqual(response.status_code, 200)