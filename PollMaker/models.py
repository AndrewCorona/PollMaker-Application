from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class PollQuestion(models.Model):
  question = models.CharField(max_length=100)

  def __str__(self):
    return self.question

class PollAnswer(models.Model):
  poll = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
  answer = models.CharField(max_length=100)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.answer

#user

#poll

#answer
 
