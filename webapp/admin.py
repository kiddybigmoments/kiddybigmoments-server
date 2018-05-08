from django.contrib import admin
from db_file_storage.form_widgets import DBAdminClearableFileInput
from django import forms
from .models import Kid, Photo, PhotoFile

admin.site.site_header = "Administración del sitio"
admin.site.site_title = admin.site.site_header


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = []
        widgets = {
            'image': DBAdminClearableFileInput
        }


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm


admin.site.register(Kid)
admin.site.register(Photo)
