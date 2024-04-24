# Create your models here.
from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    news_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):

        return self.headline

    def views_increment(self):
        self.views += 1
        self.save()

