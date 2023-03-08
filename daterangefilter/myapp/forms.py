from django import forms
from .models import *
from django.contrib.auth.models import User


class FormCreate(forms.ModelForm):
    # date = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Testtable1
        fields = ['name', 'date']
        widgets = {'date':forms.TextInput(attrs={'id':'datepicker'})}

