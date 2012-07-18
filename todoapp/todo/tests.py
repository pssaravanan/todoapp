"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from todo.models import Event, User
from django.core.exceptions import ValidationError
import unittest
class EventTestcase(unittest.TestCase):
  def test1(self):
        self.event = Event(title="some_title", description="some description")
        self.assertRaises(ValidationError, self.event.clean())

  def test2(self):
        user1 = User(user_name = "Saravanan", password="something", email = "saravananselvamani@gmail.com")
        user1.save()
        self.event = Event(title = "Some title", description="some description",
                           people_wants_to_meet="saravanan",
                           time_of_event="2012-12-18", user = user1)
        self.assertIsNone(self.event.full_clean())

