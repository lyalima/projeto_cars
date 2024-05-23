from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model_car = models.CharField(max_length=200, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand', verbose_name='Marca')
    factory_year = models.IntegerField(blank=True, null=True, verbose_name='Ano de Fabricação')
    model_year = models.IntegerField(blank=True, null=True, verbose_name='Ano do Modelo')
    value = models.FloatField(blank=True, null=True, verbose_name='Valor')
    photo = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name='Foto')
    bio = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.model_car
    
class CarInventory(models.Model):
    cars_count = models.IntegerField(blank=True, null=True)
    cars_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value} - {self.created_at}'



    
