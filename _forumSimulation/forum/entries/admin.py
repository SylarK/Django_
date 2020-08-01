from django.contrib import admin

# Register your models here.

from entries.models import Posts
from entries.models import Comment


admin.site.register(Posts)
admin.site.register(Comment)