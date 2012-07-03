from django.db import models

# Create your models here.
class Event(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  people_wants_to_meet = models.CharField(max_length = 500)
  time_of_event = models.DateTimeField(auto_now=False, auto_now_add=False)
