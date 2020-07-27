from django.contrib import admin

from users.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')


admin.site.register(Produto, ProdutoAdmin)