from django.contrib import admin
from cars.models import Car, Brand, CarInventory

#configurar como a tabela cars vai ser mostrada na página de admin do django
class CarAdmin(admin.ModelAdmin):
    #informarções da tabela que serão mostradas na página de admin para cadastrar um carro
    list_display = ('model_car', 'brand', 'factory_year', 'model_year', 'value')

    #vai permitir buscar um carro através do seu modelo ou de sua marca
    search_fields = ('model_car', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at') 
 

#vai executar as configurações anteriores definidas
admin.site.register(Car, CarAdmin)

admin.site.register(Brand, BrandAdmin)

admin.site.register(CarInventory, CarInventoryAdmin)