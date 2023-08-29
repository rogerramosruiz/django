from django import forms
from .models import Corredor

class CorredorForm(forms.ModelForm):
    codigo = forms.CharField(max_length=10, widget=forms.widgets.TextInput(attrs={"placeholder": "123", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    nombreCompleto = forms.CharField(label="Nombre completo", widget=forms.widgets.TextInput(attrs={"placeholder": "OFICINA", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    comision = forms.DecimalField(max_digits=16, decimal_places=2, widget=forms.widgets.NumberInput(attrs={"placeholder": "10.0", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    codigoAPS = forms.CharField(max_length=4,   label="Codigo APS",widget=forms.widgets.TextInput(attrs={"placeholder": "C01", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
   
    class Meta:
        model = Corredor
        fields = ('codigo', 'nombreCompleto', 'comision','codigoAPS')