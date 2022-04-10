from distutils.command.upload import upload
from django.db import models


class Picture_type(models.Model):
    name = models.CharField(max_length=30, null=False)
    def __str__(self):
        return self.name

class Pictures(models.Model):
    image = models.ImageField("Img", upload_to="images/")
    name = models.CharField("Nomi", max_length=30)
    type = models.ForeignKey(Picture_type, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name