from django.shortcuts import render,get_object_or_404
from . import models

def homepage(request):
    products = models.Product.objects.all()

    return render(request,'home.html',{'products':products})


def product_detail(request,id):
    product = get_object_or_404(models.Product,id=id)

    return render(request,'product_detail.html',{'product':product})

