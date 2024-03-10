# Create your models here.
from django.db import models


class News(models.Model):
    category = models.CharField(max_length=100)
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
