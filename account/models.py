from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError("Этот email уже используется!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password) 
        user.save()
        return user
    
    def create_user(self, email, password, **extra):
        user = self._create_user(email, password, **extra)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra):
        extra.setdefault('is_active', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra)


    
class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    phone_number= models.CharField(max_length=30, verbose_name='Номер телефона')
    count = models.PositiveIntegerField(default=0, blank=True, verbose_name='Кол-во сделок')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Менеджера'
        verbose_name_plural = 'Менеджеров'

    def __str__(self) -> str:
        return self.email


class Client(models.Model):
    full_name = models.CharField(max_length=150, blank=True, verbose_name='ФИО')
    phone_number= models.CharField(max_length=30, verbose_name='Номер телефона')    
    contract_number = models.CharField(max_length=30, verbose_name='Номер договора')    

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиентов'

    def __str__(self) -> str:
        return self.full_name
