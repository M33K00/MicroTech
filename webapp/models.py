from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'manufacturers'

    def __str__(self):
        return self.name


class RamManufacturer(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'rammanufacturers'

    def __str__(self):
        return self.name


class PSUManufacturer(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'PSUmanufacturers'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'suppliers'

    def __str__(self):
        return self.name


class Processor(models.Model):
    name = models.CharField(max_length=50)

    productcode = models.CharField(max_length=200)
    quantity = models.IntegerField()
    manufacturer = models.ForeignKey(
        'Manufacturer', on_delete=models.SET_NULL, blank=True, null=True)
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Motherboard(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        'Manufacturer', on_delete=models.SET_NULL, blank=True, null=True)
    productcode = models.CharField(max_length=200)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GraphicsCard(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        'Manufacturer', on_delete=models.SET_NULL, blank=True, null=True)
    productcode = models.CharField(max_length=200)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ram(models.Model):
    name = models.CharField(max_length=50)
    rammanufacturer = models.ForeignKey(
        'RamManufacturer', on_delete=models.SET_NULL, blank=True, null=True)
    productcode = models.CharField(max_length=200)
    capacity = models.CharField(max_length=50)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PowerSupply(models.Model):
    name = models.CharField(max_length=50)
    PSUmanufacturer = models.ForeignKey(
        'PSUManufacturer', on_delete=models.SET_NULL, blank=True, null=True)
    productcode = models.CharField(max_length=200)
    wattage = models.CharField(max_length=10)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Power Supplies'

    def __str__(self):
        return self.name
