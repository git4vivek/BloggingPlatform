from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#this just creates an profile object when user object is created
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#this saves profile object
@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

