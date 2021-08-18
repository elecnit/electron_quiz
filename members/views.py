from django.shortcuts import render
from django.views.generic  import CreateView
from .forms import SignUpFrom
from django.urls import reverse_lazy
# Create your views here.


class UserCreationView(CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')