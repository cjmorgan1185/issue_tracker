from django.test import TestCase
from .models import Ticket

class TestTicketModel(TestCase):
    def test_upvote_defaults_to_zero(self):
        ticket = Ticket(name="create a test")
        ticket.save()
        self.assertEqual(ticket.name, "create a test")
        self.assertEqual(ticket.upvotes, 0)
        
    def test_views_defaults_to_zero(self):
        ticket = Ticket(name="create a test")
        ticket.save()
        self.assertEqual(ticket.name, "create a test")
        self.assertEqual(ticket.views, 0)
        
    def test_name_as_a_string(self):
        ticket = Ticket(name="Create a Test")
        self.assertEqual("Create a Test", str(ticket))