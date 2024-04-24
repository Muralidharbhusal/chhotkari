from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet
from . import views

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'news', NewsViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('news/create/', NewsViewSet.as_view({'post': 'create'}), name='news-create'),
    path('login/', views.index, name='index'),
    path('login/home/', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('news/<int:news_id>/image/', views.get_news_image, name='get_news_image'),
    path('news/category/<str:category>/', views.get_news_by_category, name='news-by-category'),  # Endpoint to get news by category
              ] + router.urls

