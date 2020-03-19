from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse
from .forms import TopicForm
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    assert isinstance(request,HttpRequest)
    return render(request,'index.html')
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'topics.html',context)
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'topic.html',context)
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.save()
            print("topic")
            return HttpResponseRedirect(reverse('app:topics'))
    context = {'form':form}
    return render(request,'new_topic.html',context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            print("entry")
            return HttpResponseRedirect(reverse('app:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'new_entry.html',context)
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    print(request.method)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        print(form.is_valid)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:topic',args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'edit_entry.html',context)

