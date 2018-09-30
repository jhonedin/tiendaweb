from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'tienda_app/home.html',{})


def products(request):
    return render(request, 'tienda_app/products.html',{})


