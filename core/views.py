from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView


# HOME VIEW

class HomeView(TemplateView):
    template_name = 'core/home.html'

# BODEGA VIEW
class BodegaView(TemplateView):
    template_name = 'core/bodega.html'

# VARIETALES VIEW
class VarietalesView(TemplateView):
    template_name = 'core/varietales.html'

# EXPERIENCIAS VIEW
class ContactoView(TemplateView):
    template_name = 'core/contacto.html'



# REGISTER VIEW
class RegisterView(View):
    def get(self, request):
        data = {
            'form': RegisterForm()
        }

        return render(request, 'registration/register.html', data)
    
    def post(self,request):
        user_creation_form = RegisterForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
        data = {
            'form': user_creation_form
        }
        return render(request, 'registration/login.html')

