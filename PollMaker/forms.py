from django import forms
from django.forms import ModelForm
from .models import PollQuestion, PollAnswer

class QuestionForm(ModelForm):
    class Meta:
        model = PollQuestion
        fields = ['question'] 

class AnswerForm(ModelForm):
    class Meta:
        model = PollAnswer
        fields = ['answer']