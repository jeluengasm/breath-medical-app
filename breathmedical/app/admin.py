from django.contrib import admin

from .models import *

from user.models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'population',
    )

    search_fields = (
        'name',
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'population',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'country',
    )


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'legal_id',
        'address',
        'phone_number',
        'city',
    )

    search_fields = (
        'name',
        'legal_id',
    )

    list_filter = (
        'city',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'created_at',
                    'name',
                    'legal_id',
                    'address',
                    'city',
                    'phone_number',
                    'medical_areas',
                )
            },
        ),
        (
            'Users',
            {
                'fields': (
                    'patients',
                    'doctors',
                )
            },
        ),
    )

    readonly_fields = (
        'created_at',
    )

    filter_horizontal = (
        'patients',
        'doctors',
        'medical_areas',
    )

@admin.register(MedicalArea)
class MedicalAreaAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
    )


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = (
        'audio_filename',
        'user_history',
        'instrument',
        'city',
        'chest_location',
        'mode',
        'comments',
    )

    list_filter = (
        'city',
        'chest_location',
        'mode',
    )

    fieldsets = (
        (
            None, 
                {
                    "fields": (
                        'audio_filename',
                        'user_history',
                        'instrument',
                        'city',
                        'chest_location',
                        'mode',
                        'file',
                        'comments',
                    ),
                }
        ),
    )

    readonly_fields = (
        'user_history',
    )

    # search_fields = (
    #     'user_history',
    # )


    # def has_add_permission(self, request):
    #     return False

    # def has_change_permission(self, request, obj):
    #     return False

    # def has_delete_permission(self, request, obj):
    #     return False


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = (
        'audio',
        'numestdo',
        'begin_cycle',
        'end_cycle',
        'status',
    )

    list_filter = (
        'status',
    )

    fieldsets = (
        (
            None, 
            {
                "fields": (
                    'audio',
                    'numestdo',
                    'begin_cycle',
                    'end_cycle',
                    'diagnosis',
                    'variance',
                    'range_cycle',
                    'sma_coarse',
                    'sma_fine',
                    'avg_spectre',
                ),
            }
        ),
    )

    # readonly_fields = (
    #     'audio',
    #     'numestdo',
    #     'interval',
    #     'status',
    #     'variance',
    #     'range_cycle',
    #     'sma_coarse',
    #     'sma_fine',
    #     'avg_spectre',
    # )

    # search_fields = (
    #     'audio',
    # )

    # def has_add_permission(self, request):
    #     return False

    # def has_change_permission(self, request, obj):
    #     return False

    # def has_delete_permission(self, request, obj):
    #     return False

class AudioInline(admin.StackedInline):
    model = Audio
    extra = 0


@admin.register(UserHistory)
class UserHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    fieldsets = (
        (
            None, 
            {
                "fields": (
                    'patient',
                    'doctor',
                    'suggestions',
                    'created_at',
                ),
            }
        ),
    )

    readonly_fields = (
        'created_at',
    )

    # search_fields = (
    #     'patient__name',
    #     'doctor',
    # )

    inlines = (AudioInline,)

@admin.register(MedicalInstrument)
class MedicalInstrumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
    )

    list_filter = (
        'brand',
    )

    fieldsets = (
        (
            None, 
            {
                "fields": (
                    'name',
                    'brand',
                ),
            }
        ),
    )

    # readonly_fields = (

    # )

    search_fields = (
        'name',
    )
