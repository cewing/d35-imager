from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from imager_profile.models import ImagerProfile


@receiver(post_save, sender=User)
def create_profile_for_user(sender, **kwargs):
    """Ensure that user has a related profile after save"""
    instance = kwargs.get('instance')
    if not instance or kwargs.get('raw', False):
        return
    # this is a new item but not "raw"
    try:
        instance.profile
    except ImagerProfile.DoesNotExist:
        instance.profile = ImagerProfile()
        instance.profile.save()


@receiver(post_delete, sender=ImagerProfile)
def delete_user_for_profile(sender, **kwargs):
    """Ensure that if a profile is deleted, the related user is also"""
    instance = kwargs.get('instance')
    if not instance:
        return
    try:
        instance.user.delete()
    except User.DoesNotExist:
        pass
