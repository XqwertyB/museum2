from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField



class Commodity_type(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField('Sotiladi', default=False)

    def __str__(self):
        return self.Name

class Commodity(models.Model):
    name = models.CharField(max_length=30)
    info = RichTextField()
    data_Found = models.DateTimeField()
    buy_or_not = models.BooleanField('Sotiladi', default=False)
    author = models.CharField("Avtor", max_length=50)
    images = models.ImageField(upload_to="images/", null=True)
    type = models.ForeignKey(Commodity_type, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

