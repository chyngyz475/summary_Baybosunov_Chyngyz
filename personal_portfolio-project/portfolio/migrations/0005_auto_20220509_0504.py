# Generated by Django 3.2.13 on 2022-05-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_height',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='url_width',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(height_field='url_height', upload_to='portfolio/images/', width_field='url_width'),
        ),
    ]
