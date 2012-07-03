"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class Todo(TestCase):
  def assert_todo_object_save_with_no_validation_error(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        
