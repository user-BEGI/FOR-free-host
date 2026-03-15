from itertools import product


from blog.forms import ContactForm
from blog.models import Carusel, Product
from django.views.generic import DetailView

# Create your views here.

def index(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            form.save()
            return redirect('index')
    else:
        form=ContactForm()

    carusels=Carusel.objects.all()
    products=Product.objects.all()
    burgers=products.filter(category='b')
    snacks=products.filter(category='s')
    beverages=products.filter(category='be')
    malumot={
        'carusel':carusels,
        'products':products,
        'burgers':burgers,
        'snacks':snacks,
        'beverages':beverages,
        'form':form
    }
    return render(request,'index.html',context=malumot)

def about(request):
    return render(request,'about.html')
def contact(request):

    return render(request,'contact.html',)
def team(request):
    return render(request,'team.html')

def detail(request):
    return render(request,'detail.html')

class ProductDetail(DetailView):
    model=Product
    template_name='detail.html'

from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form=AuthenticationForm()


    return render(request,'login.html',{"form":form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    return render(request,'logout.html')