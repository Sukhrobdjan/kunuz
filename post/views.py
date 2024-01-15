from django.shortcuts import render
from .models import City, Category, News
from taggit.views import Tag


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
    new = News.objects.get(slug =slug)
    news_last = News.objects.all().order_by('created')
    news_cartegory = News.objects.filter(category = new.category)

    new.views += 1
    new.save()
    context = {
         'new': new,
         'news_last':news_last,
         'news_cartegory':news_cartegory,
     }
    
    return render(request, 'detail.html', context)


def tag_list(request, slug):
    tag = Tag.objects.get(slug = slug)
    news = News.objects.filter(tags = tag )

    context = {
        'tag': tag,
        'news': news,
    }
    return render(request, 'news_list.html', context)