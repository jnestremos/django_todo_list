from django.contrib import admin
from .models import List
from .models import Event
from .forms import AddEventForm, EditEventForm
admin.site.register(List)
admin.site.register(Event)

# Register your models here.
