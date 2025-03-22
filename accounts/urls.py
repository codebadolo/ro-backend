from django.urls import path
from .views import user_login, dashboard, user_logout
from . import views
urlpatterns = [
    path('', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('inventory/', views.inventory_dashboard, name='inventory_dashboard'),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_product/<pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<pk>/', views.delete_product, name='delete_product'),
    path('inventory/products/', views.product_list, name='product_list'),
    path('inventory/add-product/', views.add_product, name='add_product'),
]
