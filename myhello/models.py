from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    author = models.CharField(max_length=30)

