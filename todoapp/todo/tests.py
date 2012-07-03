"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from todo.models import Event
from django.core.exceptions import ValidationError

class Todo(unittest.TestCase):
  def assert_todo_object_should_not_save_with_validation_error(self):
        self.event = Event(title="some_title", description="some description")
        self.assertRaises(ValidationError, self.event.clean())

  def assert_todo_object_save_with_no_validation_error(self):
        self.event = Event(title = "Some title", description="some description",
                           people_wants_to_meet="saravanan",
                           time_of_event="2012-12-18")
        self.assertIsNone(self.event.full_clean())
