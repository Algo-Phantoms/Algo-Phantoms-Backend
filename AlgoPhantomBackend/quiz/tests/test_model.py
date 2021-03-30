from django.test import TestCase
from quiz.models import Quizzes,Category
from django.utils import timezone


# models test

class QuizTest(TestCase):


    def setUp(self):
        self.category = Category.objects.create(name="quiz")
        self.quiz = Quizzes.objects.create(
            title='quiz',
            category=self.category,
        )

    def test_course_category(self):
        quiz = Quizzes.objects.get(title='quiz')
        self.assertEqual(quiz.category_id, self.category.id)
