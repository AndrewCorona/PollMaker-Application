from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class PollModel(models.Model):
  question = models.CharField(max_length=100)
  answerone = models.CharField(max_length=50)
  answertwo = models.CharField(max_length=50)
  answerthree = models.CharField(max_length=50)
  answeronevotes = models.IntegerField(default=0)
  answertwovotes = models.IntegerField(default=0)
  answerthreevotes = models.IntegerField(default=0)

  def total(self):
    return self.answeronevotes + self.answertwovotes + self.answerthreevotes

  def answeronepercent(self):
    results = self.answeronevotes + self.answertwovotes + self.answerthreevotes
    results2 = self.answeronevotes / results
    results3 = results2 * 100
    return round(results3)

  def answertwopercent(self):
    results = self.answeronevotes + self.answertwovotes + self.answerthreevotes
    results2 = self.answertwovotes / results
    results3 = results2 * 100
    return round(results3)

  def answerthreepercent(self):
    results = self.answeronevotes + self.answertwovotes + self.answerthreevotes
    results2 = self.answerthreevotes / results
    results3 = results2 * 100
    return round(results3)

 
