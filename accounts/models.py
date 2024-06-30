from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    profile = models.ImageField(upload_to='profile', blank=True, null=True)
    email_token = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    forgot_password_token = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    groups = models.ManyToManyField(Group, related_name='user_set_custom')
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_custom')

    def __str__(self):
        return self.email
