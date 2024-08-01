from django.shortcuts import render
from . import models

def homepage(request):
    products = models.Product.objects.all()

    return render(request,'home.html',{'products':products})
