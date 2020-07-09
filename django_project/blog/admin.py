from django.contrib import admin
from .models import Post
#To allow models to integrate with admin page

admin.site.register(Post)