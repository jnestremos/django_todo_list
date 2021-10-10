from django import forms
from django.http import request
from django.shortcuts import redirect, render
from .models import List
from .models import Event
from .forms import ListForm
from .forms import EditForm
from .forms import AddEventForm
from .forms import EditEventForm

# Create your views here.

def home(request):
    if(request.method == "POST"):
        form = AddEventForm(request.POST or None)        
        if form.is_valid() and form.cleaned_data.get('pricing') > 0:
            form.save()
            all_events = Event.objects.all()
            return render (request, 'home.html', {'all_events' : all_events})
        else:
            return render (request, 'home.html', {'error' : 'Invalid price!'})
    else:
        all_events = Event.objects.all()
        return render (request, 'home.html', {'all_events' : all_events})
def about(request):
    my_name = 'Joshua N. Estremos'
    return render (request, 'about.html', {'myname' : my_name})

def contact(request):
    return render (request, 'contact-us.html', {})

def listings(request):
    if(request.method == "POST"):
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()            
            all_items = List.objects.all()
            return render (request, 'listings.html', {'user': 'Joshua Estremos', 'all_items' : all_items})
    else:
        all_items = List.objects.all()
        return render (request, 'listings.html', {'user': 'Joshua Estremos', 'all_items' : all_items})

def delete(request, list_id):    
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('listings')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('listings')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('listings')

def edit(request, event_id):
    if(request.method == "POST"):
        event = Event.objects.get(pk=event_id)
        form = EditEventForm(request.POST or None)
        if(form.is_valid() and form.cleaned_data.get('pricing') > 0):                    
            event.event_name = form.cleaned_data.get('event_name')
            event.event_location = form.cleaned_data.get('event_location')
            event.event_date = form.cleaned_data.get('event_date')
            event.event_remarks = form.cleaned_data.get('event_remarks')
            event.pricing = form.cleaned_data.get('pricing')
            event.save()
            return redirect('home')
    else:
        event = Event.objects.get(pk=event_id)
        return render(request, 'edit.html', {'event' : event})
