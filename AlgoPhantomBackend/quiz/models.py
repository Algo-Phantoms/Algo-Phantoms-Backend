from django.db import models
# Create your models here.

QUESTION_LEVEL = (
    ("Easy","Easy"),
    ("Medium","Medium"),
    ("Hard","Hard"),
)


class Category(models.Model):

    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"
        ordering=['id']

class Quizzes(models.Model):

    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "Quiz"
        verbose_name_plural= "Quizzes"
        ordering=['id']


class Question(models.Model):

    quiz=models.ForeignKey(Quizzes,on_delete=models.DO_NOTHING,related_name='question')
    title=models.CharField(max_length=255)
    level=models.CharField(max_length=255,choices=QUESTION_LEVEL)
    date_created=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Question"
        verbose_name_plural= "Questions"
        ordering=['id']


class Answer(models.Model):

    question=models.ForeignKey(Question,related_name='answer',on_delete=models.DO_NOTHING)
    answer_text=models.CharField(max_length=255, verbose_name="Answer Text")
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name= "Answer"
        verbose_name_plural= "Answers"
        ordering=['id']

 

