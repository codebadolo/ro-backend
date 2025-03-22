from django.core.management.base import BaseCommand
from inventory.models import ( 
                              Category, Brand, ProductType, Product,
                              ProductInventory, SpecificationGroup,
                              Specification, Stock ,ProductAttribute ,ProductAttributeValues,
                              Media
                              
)

class Command(BaseCommand):
    help = 'Deletes categories, brands, product types, and related data (excluding users).'

    def handle(self, *args, **kwargs):
        # Delete all records in the specified tables
        Category.objects.all().delete()
        Brand.objects.all().delete()
        Stock.objects.all().delete()
        ProductType.objects.all().delete()
        Product.objects.all().delete()
        ProductInventory.objects.all().delete()
        SpecificationGroup.objects.all().delete()
        Specification.objects.all().delete()
        Stock.objects.all().delete()
        ProductAttribute.objects.all().delete()
        ProductAttributeValues.objects.all().delete()
        Media.objects.all().delete()
        ProductType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all specified records.'))
