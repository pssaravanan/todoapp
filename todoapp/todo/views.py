# Create your views here.
from django.shortcuts import render_to_response
from todo.forms import EventForm 
def new(request):
  form = EventForm()
  return render_to_response('new.html', {'form': form})

def create(request):
  form = EventForm(request.POST)
  return render_to_response('new.html', {'form': form})


