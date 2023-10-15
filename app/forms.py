from django import forms
from .models import Food, Categories

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields ='__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields ='__all__'