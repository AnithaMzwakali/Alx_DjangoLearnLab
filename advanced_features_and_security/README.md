# Permissions and Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py`:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created in `setup_groups.py`:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## Enforcement
Views in `bookshelf/views.py` use `@permission_required` decorators to enforce access control.

## Testing
Assign users to groups via Django Admin and verify access restrictions.
