from django.db import models
from user.models import User
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        db_table = 'Article'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False)
    category = models.ManyToManyField(Category, max_length=400)
    content = models.TextField(null=False, default='')
    create_date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, default='')

    def __str__(self):
        return f"{self.article}에 대한 댓글"