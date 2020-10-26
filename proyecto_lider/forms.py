from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm

class RegisterForm(ModelForm):

  password2 = forms.CharField(label='Confirmar password',
                              required=True,
                              widget=forms.PasswordInput(attrs={
                              'class': 'form-control',
                              'id': 'password2',
                            }))

  class Meta:
    model = User
    fields = [
      'username', 'email','password', 'password2' 
    ]
    labels = {
      'username': 'Usuario'
    }
    widgets = {
      'password': forms.PasswordInput(),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['username'].widget.attrs.update({
      'class': 'form-control', 'id': 'username'
    })

    self.fields['email'].widget.attrs.update({
      'class': 'form-control', 'id': 'email'
    })

    self.fields['email'].required = True

    self.fields['password'].widget.attrs.update({
      'class': 'form-control', 'id': 'password'
    })

  def clean_username(self):
    username = self.cleaned_data.get('username')

    if User.objects.filter(username=username).exists():
      raise forms.ValidationError('El username ya se encuentra en uso')

    return username

  def clean_email(self):
    email = self.cleaned_data.get('email')

    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('El correo ya se encuentra en uso')

    return email

  def clean(self):
    cleaned_data = super().clean() # obtiene todos los campos del formulario

    if cleaned_data.get('password2') != cleaned_data.get('password'):
      self.add_error('password2', 'El password no coindice')

  def save(self):
    return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
           )
