from django import forms
from .models import TradeLogin

class TradeLoginForm(forms.ModelForm):
    class Meta:
        model = TradeLogin
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
