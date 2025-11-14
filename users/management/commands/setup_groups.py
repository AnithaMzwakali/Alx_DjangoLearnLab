from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book  # replace with your model if different

class Command(BaseCommand):
    help = "Create user groups and assign custom permissions"

    def handle(self, *args, **kwargs):
        # Create custom permissions for Book model
        book_ct = ContentType.objects.get_for_model(Book)

        # Create permissions if they do not exist
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

        for codename, name in permissions:
            perm, created = Permission.objects.get_or_create(
                codename=codename,
                content_type=book_ct,
                defaults={"name": name}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Permission created: {codename}"))

        # Create groups and assign permissions
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(Permission.objects.filter(codename__in=perms))
            group.save()
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group created: {group_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Group updated: {group_name}"))

        self.stdout.write(self.style.SUCCESS("Groups and permissions have been set up successfully."))
