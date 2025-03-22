from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .serializers import UserSerializer, DashboardSerializer
from rest_framework.authtoken.models import Token
from inventory.forms import ProductForm , ProductInventoryForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventory.models import Product, ProductInventory, Brand  ,Stock

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.role == 'inventory':
        return render(request, 'accounts/inventory_dashboard.html')
    elif request.user.role == 'shipping':
        return render(request, 'accounts/shipping_dashboard.html')
    # Add more conditions for other roles
    else:
        return render(request, 'accounts/default_dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')




def product_list(request):
    products = Product.objects.all()
    return render(request, 'accounts/product_list.html', {'products': products})

@login_required
def inventory_dashboard(request):
    products_count = Product.objects.count()
    total_stock = sum(stock.units for stock in Stock.objects.all())
    low_stock_count = Stock.objects.filter(units__lt=10).count()
    return render(request, 'accounts/inventory_dashboard.html', {
        'products_count': products_count,
        'total_stock': total_stock,
        'low_stock_count': low_stock_count,
    })

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'accounts/product_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'accounts/add_product.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventory.forms import ProductForm, ProductInventoryForm, CategoryForm, BrandForm, ProductTypeForm


@login_required
def create_product(request):
    # Main forms
    product_form = ProductForm(request.POST or None)
    inventory_form = ProductInventoryForm(request.POST or None)

    # Dynamic addition forms
    category_form = CategoryForm(request.POST or None, prefix='category')
    brand_form = BrandForm(request.POST or None, prefix='brand')
    product_type_form = ProductTypeForm(request.POST or None, prefix='product_type')

    if request.method == 'POST':
        # Handle dynamic category creation
        if 'add_category' in request.POST and category_form.is_valid():
            category_form.save()
            return redirect('create_product')

        # Handle dynamic brand creation
        if 'add_brand' in request.POST and brand_form.is_valid():
            brand_form.save()
            return redirect('create_product')

        # Handle dynamic product type creation
        if 'add_product_type' in request.POST and product_type_form.is_valid():
            product_type_form.save()
            return redirect('create_product')

        # Handle main form submission
        if product_form.is_valid() and inventory_form.is_valid():
            product = product_form.save()
            inventory = inventory_form.save(commit=False)
            inventory.product = product
            inventory.save()
            return redirect('product_list')

    return render(request, 'accounts/create_product.html', {
        'product_form': product_form,
        'inventory_form': inventory_form,
        'category_form': category_form,
        'brand_form': brand_form,
        'product_type_form': product_type_form,
    })


@login_required
def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    inventory = ProductInventory.objects.get(product=product)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        inventory_form = ProductInventoryForm(request.POST, instance=inventory)
        if product_form.is_valid() and inventory_form.is_valid():
            product_form.save()
            inventory_form.save()
            return redirect('inventory_dashboard')
    else:
        product_form = ProductForm(instance=product)
        inventory_form = ProductInventoryForm(instance=inventory)
    return render(request, 'accounts/edit_product.html', {'product_form': product_form, 'inventory_form': inventory_form})

@login_required
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    inventory = ProductInventory.objects.get(product=product)
    product.delete()
    inventory.delete()
    return redirect('inventory_dashboard')
