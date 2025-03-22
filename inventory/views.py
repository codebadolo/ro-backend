from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Stock
# Create your views here.
def low_stock_view(request):
    low_stock_items = Stock.objects.filter(units__lt=10)
    return HttpResponse(f"Low stock items: {low_stock_items.count()}")