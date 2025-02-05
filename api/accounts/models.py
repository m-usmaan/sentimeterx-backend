import zoneinfo

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.files.storage import FileSystemStorage
from django.db import models

from api.organizations.models import Organization
from utils.validators import CustomUsernameValidator

TIMEZONES_CHOICES = [(tz, tz) for tz in zoneinfo.available_timezones()]

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username and not email:
            raise ValueError('Username and Email are required')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Only for createsuperuser management command
    username_validator = CustomUsernameValidator()

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(
        max_length=150, validators=[username_validator], unique=True,
        error_messages={'unique': 'A user with that username already exists.'},
        help_text='Required. 150 characters or fewer. Letters, digits and ./_ only.'
    )
    email = models.EmailField(unique=True)
    avatar = models.ImageField(storage=FileSystemStorage(), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'users'
    
    @property
    def full_name(self):
        return f'{(self.first_name or "").strip()} {(self.last_name or "").strip()}'.strip()
    
    def __str__(self):
        result = f'{self.username}'
        if self.organization:
            result += f' | {self.organization}'
        
        return result


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    timezone = models.CharField(
        max_length=50,
        default=settings.TIME_ZONE,
        choices=TIMEZONES_CHOICES,
    )

    class Meta:
        db_table = 'user_profiles'
    
    def __str__(self):
        return f'{self.user}'
