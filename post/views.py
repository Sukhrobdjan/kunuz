from django.shortcuts import render
from .models import City, Category, News

def category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return context

def city(request):
    cities = City.objects.all()

    context = {
        'cities': cities,
    }

    return context


def news_list(request):
    news = News.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'news_list.html', context)


def city_news(request, slug):
    city = City.objects.get(slug = slug)
    news = News.objects.filter(city = city)

    context = {
        'news': news,
        'city': city,
    }

    return render(request,'city_news.html',  context)



def category_news(request, slug):
    category = Category.objects.get(slug = slug)
    news = News.objects.filter(category = category)

    context = {
        'news': news,
        'category': category,
    }

    return render(request,'category.html',  context)

def new_detail(request, slug):
    info = News.objects.all()
    context = {
         'info': info,
     }
    
    return render(request, 'detail.html', context)


