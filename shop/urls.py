from django.urls import path
from . import views


urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('product/<int:id>',views.product_detail,name='detail'),
]