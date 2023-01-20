from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory, UserCategory

MODELS = [Author, Category, Post, Comment, PostCategory, UserCategory]
for model in MODELS:
    admin.site.register(model)

