from django.contrib import admin
from .models import Sponser,Writing_About,Rule,Ranking,Champion,Title,Book,Equipment,Payment

admin.site.register(Sponser)

@admin.register(Champion)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','sport_name','event',)
    search_fields = ('name','sport_name','event',)
    list_filter = ('sport_name',)
    ordering = ('sport_name',)
    

@admin.register(Writing_About)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
        
@admin.register(Payment)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','entry_for','payment_status')
    search_fields = ('name','entry_for',)
    list_filter = ('entry_for','payment_status')
    ordering = ('-payment_status',)
        
@admin.register(Equipment)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name',)
    search_fields = ('name','caption',)
    ordering = ('-id',)

@admin.register(Rule)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','caption')
    search_fields = ('name','caption',)
    ordering = ('-id',)

@admin.register(Ranking)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','category')
    search_fields = ('name','category',)
    list_filter = ('category',)
    ordering = ('-id',)

@admin.register(Title)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)

@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
# Register your models here.
