from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create manager model
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    # define create_user() with parameters: name, email, password, by default, password can be empty
    def create_user(self, name, email, password = None):

        # if email is passed as empty, then use raise ValueError to print out User must have an email address
        if not email:
            raise ValueError('User must have an email address')

        # assign normalized email to email
        email = self.normalize_email(email)

        # create a new user with name and email by self.model()
        user = self.model(name = name, email = email)

        # use builtin set_password to encrypt password
        user.set_password(password)

        # save user
        user.save(using = self._db)

        return user

    # define create_superuser() with parameters: name, email, password
    def create_superuser(self, name, email, password):
        # call create_user() to create a new user
        user = self.create_user(name, email, password)

        # set the user as super user
        user.is_superuser = True

        # set the user as staff
        user.is_staff = True

        # save and return the user
        user.save(using = self._db)
        return user

    
    pass


# Create user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DB Model for users in our system"""

    # Create email field: max length is 255, and emails should be unique
    email = models.EmailField(max_length = 255, unique = True)

    # Create name field: max length is 255, doesn't have to be unique
    name = models.CharField(max_length = 255)

    # Create is_active field to determine if the user is active or not, by default user is active
    is_active = models.BooleanField(default = True)

    # Create is_staff field to determine if the user is active or not, by default user is active
    is_staff = models.BooleanField()

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    # define get_short_name to return the user name
    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    # define __str__() to let email be printed out when print the user
    def __str__(self):
        return self.email



