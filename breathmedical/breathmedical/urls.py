from django.contrib import admin
from django.urls import path, include

admin_str = 'Breath Medical App'
admin.site.site_header = admin_str
admin.site.site_title = admin_str

urlpatterns = [
    path(
        'app/',
        include('app.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),
]
