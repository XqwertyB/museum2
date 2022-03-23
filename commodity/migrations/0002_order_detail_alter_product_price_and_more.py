# Generated by Django 4.0.3 on 2022-03-19 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.PositiveSmallIntegerField(verbose_name='Narxi')),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.order')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.PositiveSmallIntegerField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Order_details',
        ),
    ]