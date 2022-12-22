import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('text of the question', max_length=200)
    publication_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('text of the choices for each question', max_length=200)
    votes = models.IntegerField('vote count',default=0)

    def __str__(self):
        return self.choice_text