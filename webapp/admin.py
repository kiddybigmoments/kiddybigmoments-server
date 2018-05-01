from django.contrib import admin

from .models import Kid, Photo, Parents

admin.site.site_header = "Administración del sitio"
admin.site.site_title = admin.site.site_header

admin.site.register(Kid)
admin.site.register(Photo)
admin.site.register(Parents)  # , verbose_name="PA")
