from django import forms
from money.models import Category, Bill

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

class BillForm(forms.ModelForm):
    class Meta:
        fields = ("category", "value", "note")
        model = Bill
