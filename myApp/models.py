from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):   # Здесь будут новостные статьи, которые будем отображать на сайте
    title = models.CharField('Title name', max_length=100, unique=True)
    text = models.TextField('Main title text')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
