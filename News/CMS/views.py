from rest_framework import viewsets, permissions

from .serializers import NewsSerializer
from django.shortcuts import render, get_object_or_404
from .models import News
from django.http import JsonResponse


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from django.utils.timesince import timesince

# Assuming `news_article` is your news article object



# def view_news(request, news_id):
#     news_article = get_object_or_404(News, pk=news_id)
#     # Increment the view count
#     news_article.views += 1
#     news_article.save()  # Save the updated view count
#     return JsonResponse({'headline': news_article.headline, 'views': news_article.views})