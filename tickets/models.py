from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    """
    A new ticket
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    done = models.BooleanField(blank=False, default =False)
    TYPE_CHOICES = (
        ('Bug','Bug'),
        ('Feature','Feature'),
        )

    def __unicode__(self):
        return self.title