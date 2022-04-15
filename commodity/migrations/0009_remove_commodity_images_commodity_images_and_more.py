# Generated by Django 4.0.3 on 2022-04-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0008_remove_commodity_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='Images',
        ),
        migrations.AddField(
            model_name='commodity',
            name='images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Commodity_images',
        ),
    ]
