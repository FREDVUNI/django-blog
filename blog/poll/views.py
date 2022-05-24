from django.shortcuts import get_object_or_404,render,redirect
from .models import Poll
from .forms import createPollForm
from django.http import HttpResponse

def home(request):
    polls = Poll.objects.all()
    context={'polls': polls}
    return render(request,'poll/home.html',context)

def create(request):
    if request.method =="POST":
        form =createPollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = createPollForm()
    context={'form':form}
    return render(request,'poll/create.html',context)

def vote(request,poll_id):
    #using the get_object_or_404 under render  poll =Poll.get_object_or_404(Poll,pk=poll_id) 
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == "POST":
        selected = request.POST['poll']
        if selected == 'option_one':
            poll.option_count_one +=1
        elif selected == 'option_two':
            poll.option_count_two +=1
        elif selected == 'option_three':
            poll.option_count_three +=1
        else:
            return HttpResponse(400,'Invalid Form')

        poll.save()
        
        return redirect('results', poll.id)        

    context={'poll':poll}
    return render(request,'poll/vote.html',context)

def results(request,poll_id):
    poll =get_object_or_404(Poll,pk=poll_id)
    context={'poll':poll}
    return render(request,'poll/results.html',context)