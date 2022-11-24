from django.db import models
from django.contrib.auth.models import AbstractUser


from levels.models import Level
from contests.models import Contest


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codeforces_handle = models.CharField(max_length=255, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    contests_registered = models.ManyToManyField(Contest, blank=True)

    def __str__(self):
        return self.user.username