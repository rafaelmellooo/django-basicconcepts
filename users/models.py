from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='users', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
