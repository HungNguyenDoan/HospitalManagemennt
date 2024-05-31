from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class StaffManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')

        account = Account.objects.create(username=username)
        account.set_password(password)
        account.save(using=self._db)
        user = self.model(account=account, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class Position(models.Model):
    name = models.CharField(max_length=255)


class Address(models.Model):
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)

class Account(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)



class Staff(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    cid = models.CharField(unique=True, max_length=12)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = StaffManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def is_authenticated(self):
        return True
