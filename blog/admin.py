from django.contrib import admin
from .models import Post

"""Model visível na páginade administração"""
admin.site.register(Post)

# Register your models here.
