from django.contrib import admin
from .models import Category,City,News


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['title', 'slug']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug':  ('title',)}
    # raw_id_fields = ['author']
    # date_hierarchy = 'title'
    ordering = ['title',] 



@admin.register(City)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['title', 'slug']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug':  ('title',)}
    # date_hierarchy = 'title'
    ordering = ['title',] 



@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'category', 'city']
    list_filter = ['title', 'category', 'city']
    search_fields = ['title', 'category', 'city', 'tags' ]
    prepopulated_fields = {'slug':  ('title',)}
    # date_hierarchy = 'title'
    ordering = ['title',] 