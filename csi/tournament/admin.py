from django.contrib import admin
from .models import Tournament,Registration_Fee

# Register your models here.


@admin.register(Tournament)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('/static/js/tinyinject.js',)
    list_display = ('tournament_name','event_category' ,'hide_from_concluded','tournament_startdate','tournament_enddate','approved','collecting_fee')
    search_fields = ('tournament_name','event_category',)
    list_editable = ('hide_from_concluded','approved','collecting_fee',)
    ordering = ('approved','-tournament_startdate',)
    
    
@admin.register(Registration_Fee)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','event_name' ,'entry_fee','payment_status','email','phone_no')
    search_fields = ('name','event_name' ,'entry_fee','payment_status','email','phone_no','city','state')
    ordering = ('event_name','payment_status')