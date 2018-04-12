from django.db import models

# Create your models here.
## photos ---> id, title, description, createdAt, children
## users  ---> id, username password email first-name, last-name, createdAt, children
## children -> id createdAt firstName lastName


class Kid(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Nombre")
    last_name = models.CharField(max_length=20, verbose_name="Apellidos")


class Photo(models.Model):
    kids = models.ForeignKey(Kid, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    image_location = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)