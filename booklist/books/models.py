from django.db import models
from django.conf import settings
from django.urls import reverse

STATUS_CHOICES = (
    ('reading', 'Reading'),
    ('finished', 'Finished')
)

class Book(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, #'to' defines the M-2-M realationship
        on_delete=models.CASCADE, # books assc. w/ user del when usr del
        related_name="books" # optional: reverse lookup, name= plural class
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={
            "pk": self.id
        })
