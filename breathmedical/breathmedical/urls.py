from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin_str = 'Breath Medical App'
admin.site.site_header = admin_str
admin.site.site_title = admin_str

urlpatterns = [
    path(
        '',
        include('app.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)