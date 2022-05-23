from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User, Soldier

@receiver(post_save, sender=User)
def create_soldier(sender, instance, created, **kwargs):
    if created and instance.is_soldier:
        Soldier.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_soldier(sender, instance, **kwargs):
    if instance.is_soldier:
        instance.soldier.save()