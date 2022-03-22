from django.db import models
from ckeditor.fields import RichTextField

class Organization(models.Model):
    name = models.CharField("Названия Организации", max_length=100,)
    tel_number1 = models.CharField("Номер телефона", max_length=13, null=False, blank=False)
    tel_number2 = models.CharField("Номер телефона2", max_length=13, null=True, blank=True)
    adress = models.CharField("Адрес", max_length=100,)
    info = RichTextField("Информация", null=True)
    email = models.EmailField("Email pochta", null=True, )
    fax = models.CharField("Faks", max_length=9, null=True, blank=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.CharField('Sovollar', max_length=200)
    answer = models.TextField('Javoblar', null=True, blank=True)

    def __str__(self):
        return self.query


class Contacts(models.Model):
    email = models.EmailField('Elektron pochta', null=True)
    number = models.IntegerField('Tel.Nomer', null=True, blank=True)
    name = models.CharField('Ismi', max_length=30)

    def __str__(self):
        return self.name