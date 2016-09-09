from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        
        fields = [
        'product'
        ]
        labels = {
        'product': 'product'
        }
        widgets = {
        'product': forms.TextInput(attrs={'class':'form-control'})
        }