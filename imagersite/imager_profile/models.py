from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


PHOTOGRAPHY_TYPE_CHOICES = [
    ('Portrait', 'Portrait Photography'),
    ('Landscape', 'Landscape Photography'),
    ('Still-life', 'Still-life Photography'),
]


class ActiveProfileManager(models.Manager):
    """A custom model manager limited only to active profiles"""
    def get_queryset(self):
        """Filter the default queryset for active users"""
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(User)
    camera = models.CharField(
        max_length=128,
        help_text="What is the make and model of your camera?"
    )
    address = models.TextField()
    website_url = models.URLField()
    photography_type = models.CharField(
        max_length=64,
        help_text="What type of photography do you primarily make?",
        choices=PHOTOGRAPHY_TYPE_CHOICES
    )

    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_user_name() or self.user.username

    def is_active(self):
        return self.user.is_active

