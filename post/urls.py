from django.urls import path
from .views import news_list, category_news


urlpatterns = [
    path('', news_list, name='news_list' ),
    path('new/<slug:slug>', category_news, name='category_news' ),

]