from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]

@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):

    model=Answer
    fields=[
        'answer_text',
        'is_correct',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'level',
        ]
    list_display = [
        'title', 
        'quiz',
        'level',
        ]
    inlines = [
        AnswerInlineModel, 
        ] 


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_correct', 
        'question'
        ]