from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

class Commodity_images(models.Model):
    images = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Commodity_type(models.Model):
    Name = models.CharField(max_length=30)
    Status = models.BooleanField('Sotiladi', default=False)

    def __str__(self):
        return self.Name

class Commodity(models.Model):
    name = models.CharField(max_length=30)
    Info = RichTextField()
    Data_Found = models.DateTimeField()
    buy_or_not = models.BooleanField('Sotiladi', default=False)
    Author = models.CharField("Avtor", max_length=50)
    Images = models.ForeignKey(Commodity_images, on_delete=models.CASCADE,)
    Type = models.ForeignKey(Commodity_type, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

