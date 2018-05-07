from django.db import models
from db_file_storage.model_utils import delete_file, delete_file_if_needed
from users.models import CustomUser


class Parents(models.Model):
    # id = models.IntegerField(primary_key=True)   # 'max_length' is ignored when used with IntegerField
    DEFAULT_PARENTS = 1
    """
    mother = models.ForeignKey('auth.CustomUser', related_name='madre_del_niño', on_delete=models.CASCADE)
    father = models.ForeignKey('auth.CustomUser', related_name='padre_del_niño', on_delete=models.CASCADE)

    def __str__(self):
        return "Madre: {}. Padre: {}".format(self.mother.username, self.father.username)
    """


class Kid(models.Model):
    DEFAULT_KID = 1
    name = models.CharField(max_length=20, verbose_name="Nombre")

    def __str__(self):
        return "{}".format(self.first_name)


class Photo(models.Model):
    kids = models.ManyToManyField(Kid, default=Kid.DEFAULT_KID)  # on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    image = models.ImageField(upload_to='webapp.PhotoFile/bytes/filename/mimetype', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Foto llamada " + self.title

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'image')
        super(Photo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Photo, self).delete(*args, **kwargs)
        delete_file(self, 'image')


class PhotoFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

