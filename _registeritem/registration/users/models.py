from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    value = models.IntegerField(verbose_name='Preço')
    validate = models.DateField(verbose_name='Data de validade')
    img = models.CharField(max_length=500, verbose_name='URL Image')

    def __str__(self):
        return f"Produto: {self.name}, Preço: {self.value} reais"

