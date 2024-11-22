from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .choices import UserRoles


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set_permissions",  # Avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.BUYER)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username  # This is inherited from AbstractUser