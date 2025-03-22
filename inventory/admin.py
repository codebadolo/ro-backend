# admin.py
from django.contrib import admin
from .models import Category, Product, Brand, ProductAttribute, ProductType, ProductInventory, Media, Stock, Specification, SpecificationGroup, Specification
from unfold.admin import ModelAdmin , TabularInline , StackedInline
from nested_admin import NestedModelAdmin, NestedTabularInline
from django.contrib import admin
from django import forms
# Form for Specification
# Form for Specification
class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['key', 'value']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['key'].disabled = True


# Inline for Specifications
class SpecificationInline(StackedInline):
    model = Specification
    form = SpecificationForm
    extra = 1


# Inline for Specification Groups
class SpecificationGroupInline(StackedInline):
    model = SpecificationGroup
    extra = 1
    inlines = [SpecificationInline]  # Nest specifications inside groups



class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

class ProductAdmin(ModelAdmin):
    list_display = ('name', 'description', 'category', 'is_active' , 'status')
    search_fields = ('name', 'description')
    list_filter = ('category', 'is_active')
    inlines = [SpecificationGroupInline]
    

class BrandAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductAttributeAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductTypeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductInventoryAdmin(ModelAdmin):
    list_display = ('sku', 'product', 'brand', 'is_active' )
    search_fields = ('sku', 'product__name')
    list_filter = ('brand', 'is_active')

class MediaAdmin(ModelAdmin):
    list_display = ('product_inventory', 'img_url', 'alt_text')
    search_fields = ('product_inventory__sku',)

class StockAdmin(ModelAdmin):
    list_display = ('product_inventory', 'units', 'units_sold')
    search_fields = ('product_inventory__sku',)

class SpecificationAdmin(ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductInventory, ProductInventoryAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(SpecificationGroup)

