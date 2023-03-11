from django.contrib import admin
from .models import Author, Cathegory, Post, PostCathegory, Comment


admin.site.register(Author)
admin.site.register(Cathegory)
admin.site.register(Post)
admin.site.register(PostCathegory)
admin.site.register(Comment)