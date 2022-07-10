from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Patient, Doctor


# @admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'city',
        'email',
        'is_staff',
        'is_active',
    )

    
    list_filter = (
        'email',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )


    readonly_fields= (
        'created_at',
    )

    search_fields = ('email',)

    ordering = ('email',)


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'city',
        'role',
        'email',
        'is_staff',
        'is_active',
    )

    
    list_filter = (
        'medical_areas',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                    'role',
                    'medical_areas',
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'password1',
                    'password2',
                    'age',
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                    'role',
                    'medical_areas',
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    filter_horizontal = ('medical_areas',)

    readonly_fields= (
        'created_at',
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        )

    ordering = ('first_name',)


@admin.register(Patient)
class PatientAdmin(UserAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'city',
        'email',
        'is_staff',
        'is_active',
    )

    
    list_filter = (
        'is_staff',
        'is_active',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'age',
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    ('first_name', 'last_name',),
                    ('legal_id_type', 'legal_id',),
                    'password1',
                    'password2',
                    'age',
                    'address',
                    'city',
                    ('email','phone_number',),
                    'photo',
                    'created_at',
                )
            },
        ),
        (
            'Healthly information',
            {
                'fields': (
                    ('blood_type','rh_factor',),
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    readonly_fields= (
        'created_at',
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        )

    ordering = ('first_name',)