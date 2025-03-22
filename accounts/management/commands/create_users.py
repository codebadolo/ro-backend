from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Create users with different roles and permissions'

    def handle(self, *args, **options):
        # Create Groups for Roles
        inventory_group, _ = Group.objects.get_or_create(name='Inventory Managers')
        shipping_group, _ = Group.objects.get_or_create(name='Shipping Managers')
        owner_group, _ = Group.objects.get_or_create(name='Owners')

        # Create Custom Permissions
        content_type = ContentType.objects.get_for_model(CustomUser)

        inventory_permission, _ = Permission.objects.get_or_create(
            codename='manage_inventory',
            name='Can manage inventory',
            content_type=content_type,
        )

        shipping_permission, _ = Permission.objects.get_or_create(
            codename='manage_shipping',
            name='Can manage shipping',
            content_type=content_type,
        )

        view_reports_permission, _ = Permission.objects.get_or_create(
            codename='view_reports',
            name='Can view reports',
            content_type=content_type,
        )

        # Assign Permissions to Groups
        inventory_group.permissions.add(inventory_permission)
        shipping_group.permissions.add(shipping_permission)
        owner_group.permissions.add(view_reports_permission)

        # Create Users and Assign Groups
        user1 = CustomUser.objects.create_user(username='inventory_user', password='password123', role='inventory')
        user1.groups.add(inventory_group)
        self.stdout.write(self.style.SUCCESS('Inventory Manager user created'))

        user2 = CustomUser.objects.create_user(username='shipping_user', password='password123', role='shipping')
        user2.groups.add(shipping_group)
        self.stdout.write(self.style.SUCCESS('Shipping Manager user created'))

        user3 = CustomUser.objects.create_user(username='owner_user', password='password123', role='owner')
        user3.groups.add(owner_group)
        self.stdout.write(self.style.SUCCESS('Owner user created'))
