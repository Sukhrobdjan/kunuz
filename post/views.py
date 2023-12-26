from django.shortcuts import render
from .models import City, Category, News

def news_list(request):
    news = News.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'news_list.html', context)