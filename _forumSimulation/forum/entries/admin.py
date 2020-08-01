from django.contrib import admin

# Register your models here.

from entries.models import Posts
from entries.models import Comment

class viewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

admin.site.register(Posts, viewAdmin)
admin.site.register(Comment)