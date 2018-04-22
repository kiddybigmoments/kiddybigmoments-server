from django.contrib import admin

from .models import Kid, Photo, Parents

admin.site.register(Kid)
admin.site.register(Photo)
admin.site.register(Parents)  # , verbose_name="PA")
