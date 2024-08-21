from django.contrib import admin
from .models import Astronaut, Spacecraft, Mission


# Register your models here.


class AstronautAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'spacewalks',
                    'is_active'
                    )
    list_filter = ('is_active',
                   )
    search_fields = ('name',
                     'phone_number')
    ordering = ('name',
                )


class SpacecraftAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'manufacturer',
                    'launch_date')
    list_filter = ('capacity',
                   )
    search_fields = ('name',
                     )
    readonly_fields = ('updated_at',
                       )


class MissionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'status',
                    'description',
                    'launch_date')

    list_filter = ('status',
                   'launch_date'
                   )

    search_fields = ('commander__name',
                     )

    readonly_fields = ('updated_at',
                       )


