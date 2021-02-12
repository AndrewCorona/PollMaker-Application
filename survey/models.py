from django.db import models

class Survey(models.Model):
  key = models.CharField(max_length=6) # The alphanumeric key the user enters to find the survey
  question = models.CharField(max_length=100) # The primary question of the survey
  can_make_own_answer = models.BooleanField(default=False) # Whether the user can specify their own answer

class SurveyOption(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE) # The survey the option is linked to
  option = models.CharField(max_length=100) # The option text ex: 'Frequently' / 'Never' / 'Twice a week' / etc

class SurveyAnswer(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE) # The survey this users answers are linked to
  survey_option = models.ForeignKey(SurveyOption, on_delete=models.CASCADE, blank=True, null=True) # Can be null (aka, a SurveyAnswer doesn't have to be tied to a SurveyOption in the case of a 'custom answer'
  answer = models.CharField(max_length=100) # this would be 'T' or 'F' unless its a 'custom answer' in which case its a full string.

  #https://docs.djangoproject.com/en/3.1/topics/forms/
