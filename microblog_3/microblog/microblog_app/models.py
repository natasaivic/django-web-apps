from django.db import models
from django.core.files.storage import FileSystemStorage


#fs = FileSystemStorage(location='/media/photos')

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=3000)
    post_image = models.ImageField(upload_to='images/', default=0) #, storage=fs)
    created_on = models.DateTimeField(auto_now_add=True, editable=True)
    created_on.editable = True

    def __str__(self):
        return self.title
