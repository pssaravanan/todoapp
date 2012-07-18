from django import forms

class EventForm(forms.Form):
  title = forms.CharField(max_length=50)
  description = forms.CharField(widget=forms.Textarea)
  people_wants_to_meet = forms.CharField(max_length = 100)
  time_of_event = forms.DateTimeField()
