import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField('date publisheds')

    def __str__(self):
        return self.question_text

    def __unicode__(self):
        return 
    
    def was_published_recently(self):
        """
        最近の日付であることを確認する。
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __unicode__(self):
        return 

"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name
"""