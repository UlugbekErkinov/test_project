from django.contrib import admin
from .models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'text', 'date_published']
    search_fields = ['title']


admin.site.register(News, NewsAdmin)
