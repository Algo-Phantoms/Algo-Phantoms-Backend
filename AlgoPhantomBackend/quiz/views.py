from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .pagination import QuizPagePagination

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title__icontains=kwargs['topic']).order_by('?')[:1]
        serializer=RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)


class QuizQuestion(ListAPIView):
    pagination_class = QuizPagePagination
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
