from django.contrib import admin
from api.models import *

class HorchataAdmin(admin.ModelAdmin):
    list_display = ('order','credit_card', 'name', 'price', 'grade', 'date', 'AdminImage')
    list_display_links = ('name', 'date', 'AdminImage')
    list_editable = ('order', 'credit_card', 'price', 'grade')

admin.site.register(Horchata, HorchataAdmin)
