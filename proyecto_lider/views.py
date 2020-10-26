from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      messages.success(request, 'Bienvenido {}'.format(user.username))
      return redirect('index')
    else:
      messages.error(request, 'Usuario o contraseña no validos')

  return render(request, 'users/login.html', {
  })

def logout_view(request):
  logout(request)
  messages.success(request, 'Sesión cerrada exitosamente')
  return redirect('login')

def register(request):
  form = RegisterForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    user = form.save()
    if user:
      login(request, user)
      messages.success(request, 'Usuario creado exitosamente')
      return redirect('index')

  return render(request, 'users/register.html', {
    'form': form
  })