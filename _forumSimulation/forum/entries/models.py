from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Título: ')
    text = models.TextField(verbose_name='Texto: ')
    countLike = models.IntegerField(verbose_name='Likes', default=0)
    countUnlike = models.IntegerField(verbose_name='Unlike', default=0)
    created_at = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return f"{ self.title }"

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return f"Comment in post {self.post}"
    






