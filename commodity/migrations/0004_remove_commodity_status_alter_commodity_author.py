# Generated by Django 4.0.3 on 2022-04-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_remove_order_detail_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='Status',
        ),
        migrations.AlterField(
            model_name='commodity',
            name='Author',
            field=models.CharField(max_length=50, verbose_name='Avtor'),
        ),
    ]
