from django.contrib import admin
from .models import *

admin.site.register(Manufacturer)
admin.site.register(RamManufacturer)
admin.site.register(PSUManufacturer)
admin.site.register(Supplier)
admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(GraphicsCard)
admin.site.register(Ram)
admin.site.register(PowerSupply)

# Register your models here.
