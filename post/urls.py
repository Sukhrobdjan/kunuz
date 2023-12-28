from django.urls import path
from .views import news_list, category_news, city_news


urlpatterns = [
    path('', news_list, name='news_list' ),
    path('category/<slug:slug>', category_news, name='category_news' ),
    path('city/<slug:slug>', city_news, name='city_news' ),

]