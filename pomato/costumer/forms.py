from django import forms
from .models import *

class CostumerForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':''}


