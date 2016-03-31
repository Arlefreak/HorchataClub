from django.contrib import admin
from api.models import Horchata

class HorchataAdmin(admin.ModelAdmin):
    list_display = ('order','publish','credit_card', 'name', 'tweet', 'price', 'grade', 'date', 'AdminImage')
    list_display_links = ('name', 'date','tweet', 'AdminImage')
    list_editable = ('order', 'publish', 'credit_card', 'price', 'grade')

admin.site.register(Horchata, HorchataAdmin)
