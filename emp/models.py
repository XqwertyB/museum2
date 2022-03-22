from django.db import models
from ckeditor.fields import RichTextField

class Departament(models.Model):
    name = models.CharField('Nomi',max_length=30)
    info = RichTextField("Ma'lumot")
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField("Bo'lim nomi", max_length=30)
    departament = models.CharField("Bo'lim", max_length=30)

    def __str__(self):
        return self.name


class EMP(models.Model):
    FIO = models.CharField("F.I.O", max_length=35)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)
    Departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    Tel = models.CharField('Tel.Nomer', max_length=13)
    Email = models.EmailField('Elektron pochta')
    Function = models.CharField('Funksiya', max_length=30)

    def __str__(self):
        return self.FIO