from django import forms
from . import models

class Boss(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ["name", "price", "slug", "stock", "description", "thumbnail"]
        
class Boss(forms.ModelForm):
    class Meta:
        model = models.Bank_account
        fields = []