from django.shortcuts import render, redirect
from .models import PollQuestion, PollAnswer
from django.views.generic import View, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import QuestionForm, AnswerForm
from django.http import JsonResponse


class HomePageView(TemplateView):
    template_name = 'home.html'

class PollCreateView(TemplateView):
    template_name = 'pollcreation/pollcreate.html'

# need a view that has a form that saves question title into question model, and associated answers for the question in a answer model

class PollCreatedView(TemplateView):
    template_name = 'pollcreation/pollcreated.html'



class PollLookUpView(TemplateView):
    template_name = 'pollanswer/polllookup.html'

class PollResultsView(TemplateView):
    template_name = 'pollanswer/pollresults.html'

# need a view that renders the vote variable from the answer model onto the page, this shows right after finishing the voteview

class PollVoteView(TemplateView):
    template_name = 'pollanswer/pollvote.html'

# need a view that gets the question model, and answer model associated to render on the screen. The answeree can then review and select an answer to vote for, or if the boolean
# from the question model is set to true (can set own answer), then user will have the pre-set answers, as well as a empty field if they wish to create their custom answer. This 
# custom answer will append to the answer model and allow future answerees of the poll to select that option.
        


#https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#https://docs.djangoproject.com/en/3.1/topics/http/views/
