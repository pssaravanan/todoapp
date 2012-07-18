from django.db import models

# Create your models here.
class User(models.Model):
  user_name = models.CharField(max_length = 50)
  password = models.CharField(max_length = 50)
  email = models.EmailField(max_length=50)

class Event(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  people_wants_to_meet = models.CharField(max_length= 100)
  time_of_event = models.DateTimeField()
  user = models.ForeignKey(User)

