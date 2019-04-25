from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import NewTicketForm


def get_ticket(request):
    """
    Create a view that will return a list
    of Tickets that were published prior to 'now'
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.filter(created_date__lte=timezone.now()
        ).order_by('-upvotes')
    return render(request, "tickets.html", {'tickets': tickets})

def ticket_detail(request, pk):
    """
    Create a view that returns a single
    ticket  based on the  ID (pk) and
    render it to the 'ticketdetail.html' template.
    Or return a 404 error if the ticket is
    not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket': ticket})
    
    
def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket': ticket})

def create_or_edit_ticket(request, pk=None):
    """
    Create a view that allows us to create
    or edit tickets
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = NewTicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = NewTicketForm(instance=ticket)
    return render(request, 'NewTicketForm.html', {'form': form})

