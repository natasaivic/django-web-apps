from django.db import models
import datetime

class Subscription(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=True)

    # hack
    created_on.editable = True

    def __str__(self):
        return self.email
