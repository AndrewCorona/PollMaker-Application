from django.urls import path, include
from . import views
from .views import (
    HomePageView, 
    PollCreateView,
    # pollcreate,
    PollCreatedView, 
    PollAnswerView,
    PollLookUpView,
    PollResultsView,
    PollVoteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create', PollCreateView.as_view(), name='create'),
    # path('create', views.pollcreate, name='create'),
    path('created', PollCreatedView.as_view(), name='created'),
    path('answer', PollAnswerView.as_view(), name='answer'),
    path('lookup', PollLookUpView.as_view(), name='lookup'),
    path('results', PollResultsView.as_view(), name='results'),
    path('vote', PollVoteView.as_view(), name='vote')
]