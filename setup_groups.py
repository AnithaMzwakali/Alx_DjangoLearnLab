from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book  # replace with your model

class Command(BaseCommand):
    help = "Create user groups and assign custom permissions"

    def handle(self, *args, **kwargs):
        # Example permission creation
        book_ct = ContentType.objects.get_for_model(Book)

        perms = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

        for codename, name in perms:
            Permission.objects.get_or_create(
                codename=codename,
                content_type=book_ct,
                defaults={"name": name}
            )

        groups = {
            "Viewers": ["can_view"],
            "Editors": ["can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perm_list in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(Permission.objects.filter(codename__in=perm_list))
            group.save()
