from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Введите логин")
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput)
    age = forms.IntegerField(label="Введите свой возраст")