# Generated by Django 4.0.3 on 2022-03-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_faq_answer_alter_organization_fax_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Elektron pochta')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Tel.Nomer')),
                ('name', models.CharField(max_length=30, verbose_name='Ismi')),
            ],
        ),
    ]
