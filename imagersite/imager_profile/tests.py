from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@example.com".format(n))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)

    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

