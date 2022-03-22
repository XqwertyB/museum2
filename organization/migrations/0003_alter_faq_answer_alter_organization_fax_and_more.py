# Generated by Django 4.0.3 on 2022-03-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_faq_organization_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Javoblar'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='fax',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Faks'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tel_number2',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Номер телефона2'),
        ),
    ]
