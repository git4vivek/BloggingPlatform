from django.db import models
from django.utils import timezone # used for dynamic date time changes
from django.contrib.auth.models import User # for authentication user who created blog posts
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #magic methods in python
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})
