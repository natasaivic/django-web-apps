from django.db import models


class Subscribe(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=True)
    created_on.editable = True

    def __str__(self):
        return self.email


class Post(models.Model):
    text = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True, editable=True)
    created_on.editable = True

    def __str__(self):
        return self.text
