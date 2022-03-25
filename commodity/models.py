from django.db import models
from ckeditor.fields import RichTextField

class Commodity_images(models.Model):
    images = models.ImageField()
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
    Main_image = models.ImageField()
    Info = RichTextField()
    Data_Found = models.DateTimeField()
    buy_or_not = models.BooleanField('Sotiladi', default=False)
    Author = models.CharField("Avtor", max_length=50)
    # Status = models.TextField()
    Images = models.ForeignKey(Commodity_images, on_delete=models.CASCADE)
    Type = models.ForeignKey(Commodity_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

