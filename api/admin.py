from django.contrib import admin
from api.models import Horchata
from ordered_model.admin import OrderedModelAdmin

class HorchataAdmin(OrderedModelAdmin):
    list_display = (
        'move_up_down_links',
        'publish',
        'credit_card',
        'name',
        'tweet',
        'grade',
        'date',
        'AdminImage'
    )
    list_display_links = (
        'name',
        'date',
        'tweet',
        'AdminImage'
                          )
    list_editable = (
        'publish',
        'credit_card',
        'grade'
                     )

admin.site.register(Horchata, HorchataAdmin)
