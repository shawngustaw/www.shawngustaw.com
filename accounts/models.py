from __future__ import unicode_literals

import hashlib
import urllib

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.fields import BooleanField


class User(AbstractUser):

    is_owner = BooleanField(default=False)

    class Meta(AbstractUser.Meta):
                swappable = 'AUTH_USER_MODEL'

    @property
    def get_gravatar_link(self):
        default = "https://www.example.com/default.jpg"
        base_url = "https://www.gravatar.com/avatar/"
        avatar_url = base_url + hashlib.md5(self.email.lower()).hexdigest()
        avatar_url += "?"
        size = 200
        avatar_url += urllib.urlencode({'d': default, 's': str(size)})
        return avatar_url

    def clean_is_owner(self):
        if (self.is_owner and User.objects.filter(is_owner=True)
                                          .exclude(pk=self.pk)):
            raise ValidationError("Only one global blog owner allowed.")
