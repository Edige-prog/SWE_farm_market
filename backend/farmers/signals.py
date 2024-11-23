from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from .models import Farmer

@receiver(post_save, sender=User)
def create_farmer_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create a Farmer profile when a User with the role 'Farmer' is created.
    """
    if created and instance.role == 'Farmer':  # Check if the user has the Farmer role
        Farmer.objects.create(user=instance)