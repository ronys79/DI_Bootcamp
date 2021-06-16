from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# admin custom user model
class MyAccountManager(BaseUserManager):
    # creates a user:
    def create_user(self, first_name, last_name, username, email, password=None):
        # raising errors if no email or username, fields mandatory:
        if not email:
            raise ValueError('User must input an email address')
        
        if not username:
            raise ValueError('User must have username')

        user = self.model(
            # noarmalize_email makes it all lower case
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
# for setting password within this function, in-built function
        user.set_password(password)
# for creating the user
        user.save(using=self._db)
        return user

# for creating the SuperUser:
    def create_superuser(self, first_name, last_name, email, username, password):
        # using create user method to create superuser
        user = self.create_user(
            # normalize email to lower case
            email = self.normalize_email(email), 
            username = username,
            first_name = first_name, 
            last_name = last_name,
            password = password, 
        )
        # setting permsions for superuser. ore details on django documentatin
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        # creating superuser
        user.save(using=self._db)
        return user

# custom user model

class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    # required fields for creating custom user model

    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_super_admin  = models.BooleanField(default=False)

    # users log in using email instead of username_field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # tells accounts app that we are using myaccount manager for all above methods
    objects = MyAccountManager()

# this is for when returning the account object it will return email address in template
    def __str__(self):
        return self.email

# defining mandatory methods

    # if user is admin has all permisions to make changes
    def has_perm(self, perm, obj=None):
        return self.is_admin

# specify function
    def has_module_perms(self, add_label):
        return True
