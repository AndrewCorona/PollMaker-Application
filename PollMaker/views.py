from django.shortcuts import render, redirect, reverse
from .models import PollModel
from .forms import PollForm
from django.http import HttpResponse


def home(request):
    polls = PollModel.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            new_poll = form.save()
            context = {'primary_key': new_poll.pk}
            return render(request, 'pollcreation/pollcreated.html', context)
    else:
        form = PollForm()
    context = {
        'form' : form
    }
    return render(request, 'pollcreation/pollcreate.html', context)

def created(request):
    return render(request, 'pollcreation/pollcreated.html')

def results(request, poll_id):
    poll = PollModel.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }

    return render(request, 'pollanswer/pollresults.html', context)

def vote(request, poll_id):
    poll = PollModel.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'choice1':
            poll.answeronevotes += 1
        elif selected_option == 'choice2':
            poll.answertwovotes += 1
        elif selected_option == 'choice3':
            poll.answerthreevotes += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'pollanswer/pollvote.html', context)


#https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#https://docs.djangoproject.com/en/3.1/topics/http/views/
