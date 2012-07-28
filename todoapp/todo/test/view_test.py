import unittest
from django.test.client import Client
from django.test.signals import template_rendered
class EventView(unittest.TestCase):
  def test1(self):
    c = Client()
    response = c.get('/events/new')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.content.__contains__('<label for="id_title">Title:</label>'))

  def test2(self):
    c = Client()
    data_to_post = {'title': 'Agile Meeting', 'description': 'Description',
                     'people_wants_to_meet': 'Venki', 'time_of_event': '2012-12-18'}
    response = c.post('/events/create', data_to_post)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(template_rendered.sender, 'index.html')
