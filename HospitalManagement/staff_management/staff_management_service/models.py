from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StaffManager(BaseUserManager):
    def create_user(self, username, account_password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')

        account = Account.objects.create(username=username, password=account_password)
        user = self.model(account=account, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, account_password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, account_password, **extra_fields)

class FullName(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Position(models.Model):
    name_position = models.CharField(max_length=255)

class Address(models.Model):
    no_house = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Account(models.Model):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)

class Staff(AbstractBaseUser):
    full_name = models.ForeignKey(FullName, null=False, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    objects = StaffManager()

    def is_authenticated(self):
        return True

