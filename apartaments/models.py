from django.db import models

from account.models import Client
# Create your models here.



class Apartament(models.Model):


    APART_STATUS = [
        ('active', 'Активна'),
        ('reservation', 'Бронь'),
        ('purchased', 'Куплено'),
        ('installment_plan', 'Рассрочка'),
        ('barter', 'Бартер')
    ]

    apartment_number = models.CharField(max_length=30, verbose_name='Номер квартиры')
    object_name = models.CharField(max_length=30, verbose_name='Объект')    
    floor = models.CharField(max_length=30, verbose_name='Этаж')    
    square = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='КВ')
    date = models.DateField(null=True, blank=True, verbose_name='Дата')
    status = models.CharField(max_length=20, choices=APART_STATUS, default='active', verbose_name='Статус')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    client = models.OneToOneField(Client, related_name='apartamets', blank=True, null=True, verbose_name='Клиент', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    def __str__(self) -> str:
        return self.status