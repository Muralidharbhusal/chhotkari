# from django.db.models.signals import post_delete
# from django.dispatch import receiver
# from .models import News
#
# @receiver(post_delete, sender=News)
# def update_news_ids(sender, instance, **kwargs):
#     # Get the ID of the deleted news article
#     deleted_news_id = instance.id
#     # Get all news articles with IDs greater than the deleted ID
#     news_to_update = News.objects.filter(id__gt=deleted_news_id)
#     # Update the IDs of the remaining news articles
#     for news in news_to_update:
#         news.id -= 1
#         news.save()
