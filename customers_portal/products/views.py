from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from . import models

# Create your views here.
class ProductsList(ListView):
    model = models.Product
    paginate_by = 3


class FarmList(ListView):
    model = models.Product
    queryset = models.Product.objects.filter(category='Farm Land')
    paginate_by = 3


class CarcassList(ListView):
    model = models.Product
    queryset = models.Product.objects.filter(category='Carcass')
    paginate_by = 3


class About(TemplateView):
    template_name = "products/about.html"


class Contact(TemplateView):
    template_name = "products/contact.html"



class ProspectCreateView(CreateView):
    model = models.Prospect
    fields = ['first_name','last_name','estate_of_interest','phone_number','office_address','home_address']
    success_url = "about"
