from django.shortcuts import render
from .models import Survey, SurveyOption, SurveyAnswer
from django.views.generic import CreateView

def SurveyCreate(request):
    model = Survey
    template_name = 'surveycreate.html'

def SurveyCreated(request):
    model = Survey
    template_name = 'surveycreated.html'

def SurveyLookUp(request):
    model = SurveyAnswer
    template_name = 'surveylookup.html'

def SurveyAnswer(request):
    model = SurveyAnswer
    template_name = 'surveyanswer.html'

def SurveyResults(request):
    model = SurveyAnswer
    template_name = 'surveyresults.html'

def HomePage(request):
    return render(request, template_name='home.html')

#https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#https://docs.djangoproject.com/en/3.1/topics/http/views/

