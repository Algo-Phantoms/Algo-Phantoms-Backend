from rest_framework import serializers
from .models import *


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = ('title',)

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields =('answer_text','is_correct')


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model=Question
        fields = ('title','answer',)
        
        
class QuestionSerializer(serializers.ModelSerializer):

    quiz=QuizSerializer(read_only=True)
    answer=AnswerSerializer(read_only=True,many=True)

    class Meta:
        model=Question
        fields=('quiz','title','answer',)