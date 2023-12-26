from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 100, unique = True)

    def __str__(self):
        return self.title
    
class City(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 250, unique = True)

    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    created = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE, null = True, blank = True)
    views = models.IntegerField(default = 0)
    tags = TaggableManager()


    def __str__(self):
        return f" News models '{self.title}' '{self.category}' "


