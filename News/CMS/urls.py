from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'news', NewsViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('news/create/', NewsViewSet.as_view({'post': 'create'}), name='news-create'),
] + router.urls

