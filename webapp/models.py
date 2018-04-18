from django.db import models


class Kid(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Nombre")
    last_name = models.CharField(max_length=20, verbose_name="Apellidos")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Photo(models.Model):
    kids = models.ManyToManyField(Kid)  # on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    image_location = models.URLField(blank=True, null=True, verbose_name="Imagen")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Foto llamada " + self.title
