# Generated by Django 2.0.4 on 2018-04-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_remove_photo_kids'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='kids',
            field=models.ManyToManyField(to='webapp.Kid'),
        ),
    ]
