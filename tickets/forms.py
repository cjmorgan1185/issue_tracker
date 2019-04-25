from django import forms
from .models import Ticket


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('name', 'title', 'description', 'case')