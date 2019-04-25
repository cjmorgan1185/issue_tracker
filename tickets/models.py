from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    """
    A new ticket
    """
    bug = 'Bug'
    feature = 'Feature'
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    done = models.BooleanField(blank=False, default =False)
    CASE_CHOICES =(
        (bug,'Bug'),
        (feature,'Feature'),
        )
    case = models.CharField(max_length=9,
                  choices= CASE_CHOICES,
                  default="")

    def __unicode__(self):
        return self.title