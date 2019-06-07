from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpRequest
from django.template import RequestContext
from .models import Author, Product
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import ArticleSerializer
# Create your views here.




@login_required(login_url='/')
def Home(request):
    return render(request, "home.html")

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()   
    return render(request, 'register.html', {'form': form})

def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/home')
    return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'api/home.html',
        {
            'title':'Home Page',
            
        }
    )

## Webpagina die Db info laat zien ##

def dbData(request):
    Product_list = Product.objects.all() ## Article List = Variabel, Objects.all() pakt alle Artikelen in de DB ##
    return render(request, 'api/products.html', {'Product': Product_list}) ##Op de HTML bestand in Article een variable die hier de Article_list variable is ##


### BASIS API ###

