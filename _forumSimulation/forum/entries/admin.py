from django.contrib import admin

# Register your models here.

from entries.models import Posts

admin.site.register(Posts)