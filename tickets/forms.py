from django import forms
from .models import Ticket


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('name','title', 'content', 'published_date', 'TYPE_CHOICES')