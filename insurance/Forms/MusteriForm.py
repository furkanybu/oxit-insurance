from django import forms
from django.forms import ModelForm

from insurance.models import Musteri


class MusteriForm(ModelForm):
    class Meta:
        model = Musteri
        fields = {'adi', 'soyadi', 'telefon', 'cinsiyet', 'adres', 'meslek', 'tc', 'vergi_no', 'dogum_tarihi'}

        widgets = {

            'adi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adı', 'value': '', 'required': 'required'}),

            'soyadi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Soyadı', 'value': '', 'required': 'required'}),

            'telefon': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon', 'value': '', 'required': 'required'}),

            'cinsiyet': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%;'}),

            'adres': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres', 'required': 'required'}),

            'meslek': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'value': '', 'required': 'required'}),

            'tc': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'T.C. No', 'value': '', 'required': 'required'}),

            'vergi_no': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Vergi No:', 'value': '', 'required': 'required'}),

            'dogum_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

        }