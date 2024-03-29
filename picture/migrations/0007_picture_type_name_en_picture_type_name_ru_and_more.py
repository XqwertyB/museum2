# Generated by Django 4.0.3 on 2022-04-18 11:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0006_pictures_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture_type',
            name='name_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='picture_type',
            name='name_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='picture_type',
            name='name_uz',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pictures',
            name='name_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='name_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='name_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='title_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Info'),
        ),
    ]
