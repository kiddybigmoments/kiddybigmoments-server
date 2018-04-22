from django.db import models


class Parents(models.Model):
    mother = models.ForeignKey('auth.User', related_name='madre_del_niño', on_delete=models.CASCADE)
    father = models.ForeignKey('auth.User', related_name='padre_del_niño', on_delete=models.CASCADE)

    def __str__(self):
        return "Madre: {}. Padre: {}".format(self.mother.username, self.father.username)


class Kid(models.Model):
    parents = models.ForeignKey(Parents, related_name='padre_del_niño', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name="Nombre")
    last_name = models.CharField(max_length=20, verbose_name="Apellidos")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Photo(models.Model):
    # owner = models.ForeignKey('auth.User', related_name='propietario_de_la_foto', on_delete=models.CASCADE)
    kids = models.ManyToManyField(Kid)  # on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    image_location = models.URLField(blank=True, null=True, verbose_name="Imagen")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Foto llamada " + self.title
