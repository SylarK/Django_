from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título: '),
    text = models.TextField(verbose_name='Texto: '),
    countLike = models.IntegerField(verbose_name='Likes', default=0),
    countUnlike = models.IntegerField(verbose_name='Unlike', default=0),
    register = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True),
    owner = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)




