from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=3000)
    #image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True, editable=True)
    created_on.editable = True

    def __str__(self):
        return self.text
