# Generated by Django 4.1.3 on 2022-12-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_space', '0006_alter_productimage_image_productcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='dream_space.product'),
        ),
    ]
