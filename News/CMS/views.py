from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import NewsSerializer
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import News
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import PostForm
from django.http import JsonResponse, HttpResponseForbidden


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


"""Belo is for front end"""




@api_view(['GET'])
def get_news_by_category(request, category):
    news = News.objects.filter(category=category).order_by('-created_at')
    serializer = NewsSerializer(news, many=True)


    return Response(serializer.data)


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
            print("return Successfully added")
            return redirect('login/home')  # Redirect to the dashboard or post list page

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


def get_news_image(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    if news_item.image:
        with open(news_item.image.path, 'rb') as image_file:
            return HttpResponse(image_file.read(), content_type='image/jpeg')  # Adjust content type as needed
    else:
        return HttpResponse(status=404)
