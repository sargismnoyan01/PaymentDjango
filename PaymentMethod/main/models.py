from django.db import models

class Product(models.Model):
    name=models.CharField('Product name',max_length=255)
    img = models.ImageField('image',upload_to='products')
    price = models.IntegerField('Price')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'