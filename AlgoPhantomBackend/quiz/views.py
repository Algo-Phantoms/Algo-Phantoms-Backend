from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from .pagination import QuizPagePagination, PaginationHandlerMixin

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title__icontains=kwargs['topic']).order_by('?')[:1]
        serializer=RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)


class QuizQuestion(APIView, PaginationHandlerMixin):
    pagination_class = QuizPagePagination
    serializer_class = QuestionSerializer

    # def get(self, request, format=None, **kwargs):
    #     quiz = Question.objects.filter(quiz__title__icontains=kwargs['topic'])
    #     serializer = QuestionSerializer(quiz, many=True)
    #     return Response(serializer.data)

    def get(self, request, format=None, *args, **kwargs):
        instance = Question.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)