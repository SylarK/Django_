from django.contrib import admin

from users.models import Usuario

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(Usuario, UsersAdmin)
