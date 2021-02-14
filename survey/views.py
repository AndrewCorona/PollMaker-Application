from django.shortcuts import render
from .models import Survey, SurveyOption, SurveyAnswer
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class SurveyCreateView(TemplateView):
    template_name = 'surveycreation/surveycreate.html'

class SurveyCreatedView(TemplateView):
    template_name = 'surveycreation/surveycreated.html'

class SurveyAnswerView(TemplateView):
    template_name = 'surveyanswer/surveyanswer.html'

class SurveyAnswerKeyView(TemplateView):
    template_name = 'surveyanswer/surveyanswerkey.html'

class SurveyLookUpView(TemplateView):
    template_name = 'surveyanswer/surveylookup.html'

class SurveyResultsView(TemplateView):
    template_name = 'surveyanswer/surveyresults.html'

#https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#https://docs.djangoproject.com/en/3.1/topics/http/views/

