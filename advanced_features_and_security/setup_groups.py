# advanced_features_and_security/setup_groups.py
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

def setup_groups():
    # Get permissions
    can_view = Permission.objects.get(codename="can_view")
    can_create = Permission.objects.get(codename="can_create")
    can_edit = Permission.objects.get(codename="can_edit")
    can_delete = Permission.objects.get(codename="can_delete")

    # Create groups
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    viewers.permissions.set([can_view])
    editors.permissions.set([can_view, can_create, can_edit])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])
