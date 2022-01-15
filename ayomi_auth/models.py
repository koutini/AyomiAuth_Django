from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    """Contain the definition of profile model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birthday = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_profile_signal(sender, instance, created, **kwargs):
    """Signal to create profile when user created"""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
