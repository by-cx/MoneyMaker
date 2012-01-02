from django import forms
from money.models import Category, Bill

class CategoryForm(forms.ModelForm):
    display_name = "Category"

    class Meta:
        model = Category

class BillForm(forms.ModelForm):
    display_name = "Bill"

    class Meta:
        fields = ("category", "value", "note")
        model = Bill
