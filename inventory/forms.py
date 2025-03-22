from django import forms
from .models import Product, ProductInventory, Brand , Category , ProductType

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category')
        
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError(
                "Category not found. Click the '+' button to add a new category."
            )
        return category    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['name']
class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        fields = ('sku', 'upc', 'product_type', 'brand', 'retail_price', 'store_price', 'is_digital', 'weight')
        
        
        
        

        