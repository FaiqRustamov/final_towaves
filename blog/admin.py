from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug' : ('Title',)}
    list_display = ('Title', 'Tag', 'Date')
    search_fields = ['Title', 'Tag' 'Slug', 'Content']
    list_filter = ('Title', 'Tag',)

admin.site.register(Blog, BlogAdmin)

admin.site.register(Event)
admin.site.register(Category)
