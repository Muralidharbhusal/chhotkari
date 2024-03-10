from rest_framework import viewsets, permissions

from .serializers import NewsSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.shortcuts import render
from .forms import PostForm
from django.http import JsonResponse, HttpResponseForbidden


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from django.utils.timesince import timesince

# Assuming `news_article` is your news article object
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'dashboard.html')


def view_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.increment_views()  # Increment views count

# views.py


def create_post(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the post using your API
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or post list page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
    # else:
    #     return HttpResponseForbidden("You are not authorized to access this page.")


# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard or any other page
                return redirect('home')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'home.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'home.html', {'form': form})
