from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Enter your name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Enter your surname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control", "placeholder": "Enter your email"}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your address"
    }))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "address")
