from django.shortcuts import render,redirect
from .models import Topics, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

"""Rnedering the home page"""

def index(request):
    return render(request,'index.html')


"""Rendering the list of topics"""
@login_required
def topics(request):
    """Show all the topics"""
    topics = Topics.objects.filter(owner=request.user).order_by('date_added')
    context = {"topics":topics}
    return render(request,'topics.html',context)

"""Rendering the entries to a coressponding topic"""
@login_required
def individual_topic(request,topic_id):
    """Show a single topic and all its entries"""
    topic = Topics.objects.get(id=topic_id)
    # Make sure that topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'individual_topic.html',context)

"""Adding a new topic"""
@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted, create a empty form
        form = TopicForm()
    else:
        # POST data submitted, process the data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_log:topics')
        # Display a blank or invalid form
    context = {'form':form}
    return render(request,'new_topic.html',context)

"""Adding a new entry"""
@login_required
def new_entry(request,topic_id):
    """Add a new entry for a particular topic"""
    topic = Topics.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # Post data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_log:individual_topic',topic_id = topic_id)

    # Display a blank or invalid form
    context = {'topic':topic,'form':form}
    return render(request,'new_entry.html',context)

"""Edit an entry"""
@login_required
def edit_entry(request,entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # initial request, prefill the form with the existing entry
        form = EntryForm(instance=entry)
    else:
        # Post data submitted, process data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log:individual_topic',topic_id = topic.id)
    context = {'entry':entry, 'topic':topic,'form':form}
    return render(request,'edit_entry.html',context)

"""Delete a topic"""
@login_required
def delete_topic(request,topic_id):
    topic = Topics.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    topic.delete()
    return redirect('learning_log:topics')

"""Delete an entry"""
@login_required
def delete_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic= entry.topic
    if topic.owner != request.user:
        raise Http404
    entry.delete()
    return redirect('learning_log:individual_topic',topic.id)
