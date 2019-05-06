from django.contrib import admin
from masterpage.models import Sports
from masterpage.models import Entertainment
from masterpage.models import Politics
from masterpage.models import Editorials

class SportsAdmin(admin.ModelAdmin):
    list_display=['title']

admin.site.register(Sports,SportsAdmin)

class  EntertainmentAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Entertainment,EntertainmentAdmin)

class PoliticsAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Politics,PoliticsAdmin)

class EditorialsAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Editorials,EditorialsAdmin)
