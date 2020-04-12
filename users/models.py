from django.conf import settings
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='users', null=True, blank=True)

    @property
    def avatar_url(self):
        return settings.MEDIA_URL + str(self.avatar)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
