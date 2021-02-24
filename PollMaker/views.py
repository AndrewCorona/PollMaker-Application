from django.shortcuts import render, redirect
from .models import PollQuestion, PollAnswer
from django.views.generic import View, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import QuestionForm, AnswerForm


class HomePageView(TemplateView):
    template_name = 'home.html'

class PollCreateView(TemplateView):
    template_name = 'pollcreation/pollcreate.html'

    def pollcreate(request):
        if request.method == "POST":
            question_form = QuestionForm(request.post)
            answer_form = AnswerForm(request.post)

            if question_form.is_valid() and answer_form.is_valid():
                poll = question_form.save()
                pollanswer = answer_form.save(False)
                
                pollanswer.poll=poll
                pollanswer.save()

                return redirect(reverse('PollMaker.views.PollCreatedView'))

        else:
            question_form = QuestionForm()
            answer_form = AnswerForm()
        
        return render(request, "pollcreation/pollcreate.html", {'question_form':question_form, 'answer_form':answer_form})

class PollCreatedView(TemplateView):
    template_name = 'pollcreation/pollcreated.html'

class PollAnswerView(TemplateView):
    template_name = 'pollanswer/pollanswer.html'
    model = PollQuestion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll_displayquestion'] = PollQuestion.objects.all
        context['poll_displayanswers'] = PollAnswer.objects.all
        return context

class PollLookUpView(TemplateView):
    template_name = 'pollanswer/polllookup.html'

class PollResultsView(TemplateView):
    template_name = 'pollanswer/pollresults.html'

class PollVoteView(TemplateView):
    template_name = 'pollanswer/pollvote.html'


#https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#https://docs.djangoproject.com/en/3.1/topics/http/views/
