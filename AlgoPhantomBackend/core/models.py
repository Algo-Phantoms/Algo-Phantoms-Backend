from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Quizzes
# Create your models here.

class quizScore(models.Model):
	score = models.IntegerField(default=0)
	maximum_score = models.IntegerField(default=0)
	is_cleared = models.BooleanField(default=False)
	user = models.ForeignKey('auth.User', related_name='quizscore', on_delete=models.CASCADE, blank=True, null=True)
	quiz = models.ForeignKey(Quizzes, related_name='quizscore', on_delete=models.CASCADE, blank=True, null=True)