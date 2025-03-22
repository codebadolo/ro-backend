import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from faker import Faker
from inventory.models import (
    Category,
    Product,
    ProductType,
    SpecificationGroup,
    Specification,
    ProductInventory,
    Stock,
)

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with 500 products and related data.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to populate the database...")

        # Step 1: Create categories and subcategories
        self.create_categories()

        # Step 2: Create product types
        self.create_product_types()

        # Step 3: Create products with specifications and inventories
        self.create_products(500)

        self.stdout.write("Database population completed successfully.")

    def create_categories(self):
        self.stdout.write("Creating categories...")
        categories = {
            "Computer Science": ["Algorithms", "Artificial Intelligence", "Cybersecurity", "Software Engineering"],
            "Networks": ["Network Protocols", "Cloud Computing", "Wireless Networks"],
            "Electronic Devices": ["Microcontrollers", "IoT Devices", "Sensors"],
            "Software": ["Operating Systems", "Database Systems", "Development Tools"],
        }

        for category_name, subcategories in categories.items():
            parent_category = Category.objects.create(
                name=category_name,
                slug=fake.slug(),
                is_active=True,
            )
            for subcategory_name in subcategories:
                Category.objects.create(
                    name=subcategory_name,
                    slug=fake.slug(),
                    is_active=True,
                    parent=parent_category,
                )

        self.stdout.write("Categories created successfully.")

    def create_product_types(self):
        self.stdout.write("Creating product types...")
        product_types = [
            "Servers",
            "Workstations",
            "GPUs",
            "Development Boards",
            "Routers",
            "Switches",
            "Firewalls",
            "Microcontrollers",
            "Sensors",
            "Smart IoT Devices",
            "IDEs",
            "Database Management Systems",
            "Operating Systems",
            "Virtual Machines",
        ]

        for product_type in product_types:
            ProductType.objects.create(name=product_type)

        self.stdout.write("Product types created successfully.")

    def create_products(self, num_products):
        self.stdout.write(f"Creating {num_products} products...")
        categories = Category.objects.filter(parent__isnull=False)  # Only subcategories
        product_types = ProductType.objects.all()

        for _ in range(num_products):
            category = random.choice(categories)
            product_type = random.choice(product_types)

            product = Product.objects.create(
                web_id=fake.unique.bothify(text='????-########'),
                slug=fake.slug(),
                name=fake.catch_phrase(),
                description=fake.paragraph(),
                category=category,
                is_active=True,
                status="available",
            )

            # Add specifications to the product
            self.create_specifications(product)

            # Create inventory for the product
            self.create_inventory(product, product_type)

        self.stdout.write(f"{num_products} products created successfully.")

    def create_specifications(self, product):
        specification_groups = ["Performance", "Connectivity", "Power", "Compatibility"]

        for group_name in specification_groups:
            # Append a unique identifier to make the name globally unique
            unique_group_name = f"{group_name}_{product.id}_{random.randint(1, 10000)}"
            group = SpecificationGroup.objects.create(product=product, name=unique_group_name)

            specifications = {
                "Performance": [("Processor Speed", f"{random.randint(2, 5)} GHz"), ("RAM", f"{random.randint(8, 64)} GB")],
                "Connectivity": [("Ports", f"{random.randint(2, 12)} Ethernet Ports"), ("Wi-Fi Standard", random.choice(["802.11ac", "802.11n"]))],
                "Power": [("Voltage", f"{random.randint(5, 12)}V DC"), ("Power Consumption", f"{random.randint(10, 50)}W")],
                "Compatibility": [("Supported OS", random.choice(["Windows/Linux/MacOS"])), ("Architecture", random.choice(["x86/x64"]))]
            }

            for key, value in specifications.get(group_name, []):
                Specification.objects.create(group=group, key=key, value=value)



    def create_inventory(self, product, product_type):
        inventory = ProductInventory.objects.create(
            sku=fake.unique.bothify(text='SKU-########'),
            upc=fake.unique.bothify(text='UPC-########'),
            product_type=product_type,
            product=product,
            is_active=True,
            is_default=True,
            retail_price=Decimal(random.uniform(1000, 5000)),
            store_price=Decimal(random.uniform(500, 3000)),  # Ensure this value is within the allowed range
            is_digital=False,
            weight=random.uniform(0.5, 5),
        )

        Stock.objects.create(
            product_inventory=inventory,
            units=random.randint(10, 100),
            units_sold=random.randint(0, 50),
        )
