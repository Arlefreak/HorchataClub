from django.contrib import admin
from api.models import Horchata
from adminsortable2.admin import SortableAdminMixin

class HorchataAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'publish',
        'name',
        'grade',
        'date',
        'AdminImage'
    )
    list_display_links = (
        'name',
        'date',
        'AdminImage'
                          )
    list_editable = (
        'publish',
        'grade'
                     )

admin.site.register(Horchata, HorchataAdmin)
