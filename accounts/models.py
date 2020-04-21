from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, is_active=True, is_staff=False, is_admin=False, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('You must provide an email address')
        if not first_name:
            raise ValueError('You must provide a first name')
        if not last_name:
            raise ValueError('You must provide a last name')
        if not phone_number:
            raise ValueError('You must provide a contact number')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, phone_number, is_active=True, is_staff=True, is_admin=False, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone_number,
            is_active,
            is_staff,
            is_admin,
            password=password,
        )
        user.staff = is_staff
        user.active = is_active
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, is_active=True, is_staff=True, is_admin=True, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone_number,
            is_active,
            is_staff,
            is_admin,
            password=password,
        )
        user.staff = is_staff
        user.active = is_active
        user.admin = is_admin
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    default_date = datetime(year = 2019, month = 9, day = 1, hour = 0, minute = 0, second = 0)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default=''
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=18, blank=True, null=True)
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Joined on",)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.
    is_active = models.BooleanField(default=True)

    """ The is_active field above was added and the @property for def is_active, which is found on the last line of this
        file because password_reset was throwing an unusual exception  """

    objects = UserManager()
    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def get_first_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_last_name(self):
        # The user is identified by their email address
        return self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_phone_number(self):
        # The user is identified by their email address
        return self.phone_number

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active
