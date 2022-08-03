from django.db import models

# Create your models here.

# -------------- Таблица заказов ---------------------------

class Order_table(models.Model):
    serial = models.CharField(max_length=10, verbose_name='№', null=True, blank=True)
    order = models.CharField(max_length=50, verbose_name='заказ №', null=True, blank=True)
    cost_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='стоимость, $', null=True, blank=True)
    cost_rub = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='стоимость, руб', null=True, blank=True)
    delivery_time = models.CharField(max_length=20, verbose_name='срок поставки')
    delivery_time_format = models.DateField(default=None, null=True)
    exist = models.BooleanField(default=False)

# -------------- Вспомогательная таблица ---------------------------

class Auxiliary_table(models.Model):
    exchange_rate = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='курс $', null=True, blank=True)
