from django.contrib import admin
from .models import Post

# Register your models here.
# Registering the Post model to the django admin page

admin.site.register(Post)
