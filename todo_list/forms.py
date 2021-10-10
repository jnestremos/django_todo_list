from django import forms
from django.db.models import fields
from .models import Event, List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item_name', 'completed']

class EditForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item_name']

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_location', 'event_date', 'event_remarks', 'pricing']

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_location', 'event_date', 'event_remarks', 'pricing']