from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField


class Picture_type(models.Model):
    name = models.CharField(max_length=30, null=False)
    def __str__(self):
        return self.name

class Pictures(models.Model):
    image = models.ImageField("Img", upload_to="images/")
    name = models.CharField("Nomi", max_length=30)
    title = RichTextField('Info', null=True)
    type = models.ForeignKey(Picture_type, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name