from django.contrib import admin
from .models import Newse

@admin.register(Newse)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('news_title','news_category','timestamp',)
    search_fields = ('tournament_name','news_category',)
    ordering = ('-timestamp',)
    list_per_page = 25
    list_filter = ('news_category',)

# Register your models here.
