from django import forms
from cars.models import Brand, Car

'''#forma menos eficiente de criar um form e salvar os dados no bd
class CarForm(forms.Form):
    model_car = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    value = forms.FloatField()
    photo = forms.ImageField()

    #metodo save de forms.py; salva os dados que o usuario colocou no form
    def save(self):
        #cria um objeto carro com os dados que o usuario passou no form
        car = Car(
            model_car = self.cleaned_data['model_car'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        #metodo save de models.py; salva os dados no banco de dados, não é o save declarado acima
        car.save()
        return car'''

#forma mais eficiente de criar um form 
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    #validação do campo value
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo deve ser R$20.000')
        return value
    
    #validação do campo factory_year
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1900:
            self.add_error('factory_year', 'Data de fabricação mínima deve ser 1975')
        return factory_year