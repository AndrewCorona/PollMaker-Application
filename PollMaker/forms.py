from django.forms import ModelForm
from .models import PollModel

class PollForm(ModelForm):
    class Meta:
        model = PollModel
        fields = ['question', 'answerone', 'answertwo', 'answerthree'] 