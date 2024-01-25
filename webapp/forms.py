from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Processor, Motherboard, GraphicsCard, Ram, PowerSupply, Manufacturer, Supplier


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProcessorForm(forms.ModelForm):
    class Meta:
        model = Processor
        fields = ['name', 'productcode',
                  'quantity', 'manufacturer', 'supplier']


class MotherboardForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        fields = ['name', 'productcode',
                  'quantity', 'manufacturer', 'supplier']


class GraphicsCardForm(forms.ModelForm):

    class Meta:
        model = GraphicsCard
        fields = ['name', 'productcode',
                  'quantity', 'manufacturer', 'supplier']


class RamForm(forms.ModelForm):

    class Meta:
        model = Ram
        fields = ['name', 'productcode', 'capacity',
                  'quantity', 'rammanufacturer', 'supplier']


class PowerSupplyForm(forms.ModelForm):

    class Meta:
        model = PowerSupply
        fields = ['name', 'productcode', 'wattage',
                  'quantity', 'PSUmanufacturer', 'supplier']
