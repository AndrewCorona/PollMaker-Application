from django.urls import path, include
from . import views
from .views import (
    HomePageView, 
    PollCreateView,
    PollCreatedView, 
    PollLookUpView,
    PollResultsView,
    PollVoteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create', PollCreateView.as_view(), name='create'),
    path('created', PollCreatedView.as_view(), name='created'),
    path('lookup', PollLookUpView.as_view(), name='lookup'),
    path('results', PollResultsView.as_view(), name='results'),
    path('vote', PollVoteView.as_view(), name='vote')
]