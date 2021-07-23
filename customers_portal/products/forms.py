from django import forms
from products.models import Prospect


class SubcriberForm(forms.ModelForm):
    class Meta():
        model = Prospect
        fields = '__all__'
