from django.contrib import admin
from .models import Comment, Profile, Meet

# Register your models here.
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Meet)
