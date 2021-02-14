from django.urls import path, include
from .views import (
    HomePageView, 
    SurveyCreateView,
    SurveyCreatedView, 
    SurveyAnswerView,
    SurveyAnswerKeyView,
    SurveyLookUpView,
    SurveyResultsView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('surveycreate', SurveyCreateView.as_view(), name='surveycreate'),
    path('surveycreated', SurveyCreatedView.as_view(), name='surveycreated'),
    path('surveyanswer', SurveyAnswerView.as_view(), name='surveyanswer'),
    path('surveyanswerkey', SurveyAnswerKeyView.as_view(), name='surveylookupanswerkey'),
    path('surveylookup', SurveyLookUpView.as_view(), name='surveylookup'),
    path('surveyresults', SurveyResultsView.as_view(), name='surveyresults')
]