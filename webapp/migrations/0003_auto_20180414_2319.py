# Generated by Django 2.0.4 on 2018-04-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_photo_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_location',
            field=models.URLField(blank=True, null=True, verbose_name='Imagen'),
        ),
    ]