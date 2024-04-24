from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'category', 'headline','image', 'content', 'created_at', 'views', 'news_link']

