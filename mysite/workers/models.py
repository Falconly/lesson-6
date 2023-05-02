from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Worker(models.Model):
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    telephone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name="Email")
    adress = models.CharField(max_length=255, verbose_name="Адрес", blank=True)
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото сотрудника", blank=True)

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('list_workers')

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"
        ordering = ('id',)
