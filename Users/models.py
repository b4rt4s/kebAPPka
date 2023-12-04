from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    is_restricted = models.BooleanField(default=False, null=True)
    phone_number = models.CharField(max_length=20)
    newsletter_consent = models.BooleanField(default=False)
    terms_consent = models.BooleanField(default=False)
    data_processing_consent = models.BooleanField(default=False)
    # location_consent = models.BooleanField(default=False)
    # marketing_consent = models.BooleanField(default=False)

    AUTHENTICATION_TYPE_CHOICES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
    )

    authentication_type = models.CharField(max_length=10, choices=AUTHENTICATION_TYPE_CHOICES, default='email')

    objects = CustomUserManager()