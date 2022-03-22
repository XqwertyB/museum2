# Generated by Django 4.0.3 on 2022-03-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=30, verbose_name='F.I.O')),
                ('Tel', models.PositiveSmallIntegerField(default=998, verbose_name='Tel.Nomer')),
                ('Birth_D', models.PositiveSmallIntegerField(default=998, verbose_name='Tugilgan sana')),
                ('Gender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shiper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=30, verbose_name='F.I.O')),
                ('TEL', models.PositiveSmallIntegerField(default=998, verbose_name='Tel.Nomer')),
            ],
        ),
    ]
