from django.db import models
from commodity.models import Commodity



class Client(models.Model):
    FIO = models.CharField('F.I.O', max_length=30)
    Tel = models.PositiveSmallIntegerField('Tel.Nomer', default=+998)
    Birth_D = models.PositiveSmallIntegerField('Tugilgan sana', default=+998)
    Gender = models.CharField(max_length=200)

    def __str__(self):
        return self.FIO



class Shiper(models.Model):
    FIO = models.CharField('F.I.O', max_length=30)
    TEL = models.PositiveSmallIntegerField('Tel.Nomer', default=+998)

    def __str__(self):
        return self.FIO

class Product(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    Price = models.PositiveSmallIntegerField("Narxi", default=0)
    Status = models.BooleanField('Sotiladi', default=False)
    Data = models.DateTimeField("Sana", auto_now_add=True)

    def __int__(self):
        return self.commodity
class Pay(models.Model):
    Name = models.CharField('Tulov turi', max_length=30)

    def __str__(self):
        return self.Name

class Order(models.Model):
      client_id = models.ForeignKey( Client, on_delete=models.CASCADE,)
      Quanty = models.SmallIntegerField('Zakazlar soni', default=0)
      SumProce = models.SmallIntegerField('Narxi', default=0)
      Order_data = models.DateTimeField(auto_now=True)
    #   Pay_type = models.ForeignKey("Tulov turi", Pay, on_delete=models.CASCADE, null=True)
      Status = models.BooleanField('Statusi', default=False)
      Ship_id = models.ForeignKey(Shiper, on_delete=models.CASCADE, null=True)
      Ship_status = models.BooleanField(default=False)

      def __init__(self,):
          return self.client_id
          




class Order_detail(models.Model):
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    Price = models.PositiveSmallIntegerField('Narxi', default=0)
    Quanty = models.PositiveSmallIntegerField('Ekspanat soni', default=0)

    def __int__(self):
        return self.Price