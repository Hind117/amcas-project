from django.contrib import admin
from .models import Contact, Article, FilesAdmin, nasaNew, Profile, Topic, Book, Comment, MemberPost

# Register your models here.
admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(FilesAdmin)
admin.site.register(nasaNew)
admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(MemberPost)