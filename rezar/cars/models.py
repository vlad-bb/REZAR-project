from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False)


class CarShape(models.Model):  # тип кузова
    shape = models.CharField(max_length=20, blank=True)


class Engine(models.Model):
    size = models.CharField(max_length=50, blank=True)
    power_reserve = models.IntegerField(blank=True)
    speed = models.IntegerField(blank=True)


class CarModel(models.Model):
    model_name = models.CharField(max_length=50, blank=False)
    trim = models.CharField(max_length=50, blank=True)  # комплектация
    car_shape = models.ForeignKey(CarShape, to_field='id', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, to_field='id', on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, to_field='id', on_delete=models.CASCADE)


class Car(models.Model):
    price = models.IntegerField(blank=True)
    car_model = models.ForeignKey(CarModel, to_field='id', on_delete=models.CASCADE)
