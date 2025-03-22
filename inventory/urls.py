from django.urls import path
from .sites import stock_admin_site
from . import views
urlpatterns = [
path("low-stock/", views.low_stock_view),
]
