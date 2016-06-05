from __future__ import unicode_literals

import hashlib
import urllib

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def get_gravatar_link(self):
        default = "https://www.example.com/default.jpg"
        base_url = "https://www.gravatar.com/avatar/"
        # size = 40
        avatar_url = base_url + hashlib.md5(self.email.lower()).hexdigest()
        avatar_url += "?"
        # avatar_url += urllib.urlencode({'d': default, 's': str(size)})
        avatar_url += urllib.urlencode({'d': default})
        return avatar_url
