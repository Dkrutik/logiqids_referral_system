from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, city, referral_code, password=None, generated_code=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            city=city,
            referral_code=referral_code,
            generated_code=generated_code
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, city, referral_code, password=None, generated_code=None):
        user = self.create_user(email, name, city, referral_code, password, generated_code)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    generated_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'city', 'referral_code']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
