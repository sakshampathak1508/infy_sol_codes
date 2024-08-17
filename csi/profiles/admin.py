from django.contrib import admin
from .models import Player,Coache,Referee,Association,Position,Club
# admin.site.register(Coache)
# admin.site.register(Referee)

@admin.register(Player)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','gender','is_approved')
    list_editable = ('is_approved',)
    search_fields = ('name','gender')
    ordering = ('is_approved','name',)
    list_per_page = 25
    list_filter = ('gender',)
        
        
@admin.register(Coache)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','certificate',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25
        
@admin.register(Club)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    ordering = ('name',)  
        
@admin.register(Referee)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('name','certificate',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25
        
class Posline(admin.TabularInline):
    model = Association.position.through

@admin.register(Association)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyInject.js',)
    ordering = ('name',)
    inlines = (Posline,)
    exclude = ('position',)
    
@admin.register(Position)
class PostAdmin(admin.ModelAdmin):
    ordering = ('-association_name',)
    class Media:
        js= ('/static/js/tinyInject.js',)
        
        
# Register your models here.
