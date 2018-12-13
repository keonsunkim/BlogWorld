from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):

    def create_user(self, email, representation_name,
                    date_of_birth, phone_number,
                    last_name, first_name,
                    password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError_('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            representation_name=representation_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            last_name=last_name,
            first_name=first_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, representation_name,
                         date_of_birth, phone_number,
                         last_name, first_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            representation_name=representation_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            last_name=last_name,
            first_name=first_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        db_index=True
    )

    representation_name = models.CharField(verbose_name=_('unique representation name'),
                                           null=False, blank=False, max_length=30,
                                           unique=True, db_index=True)

    date_of_birth = models.DateField(verbose_name=_('date of birth'),)
    is_active = models.BooleanField(verbose_name=_('is active'),
                                    default=True)
    is_admin = models.BooleanField(verbose_name=_('is admin'),
                                   default=False)

    phone_number = models.IntegerField(verbose_name=_('phone number'),
                                       null=False, blank=False)

    last_name = models.CharField(verbose_name=_('family name'),
                                 null=False, blank=False, max_length=30)
    first_name = models.CharField(verbose_name=_('first name'),
                                  null=False, blank=False, max_length=30)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['date_of_birth', 'representation_name',
                       'phone_number', 'last_name', 'first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The use has a name!
        full_name = f'{self.last_name} {self.first_name}'
        return full_name

    def get_short_name(self):
        # The user's short name is their first name!
        return self.first_name

    def get_email(self):
        return self.eamil

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
        # Simplest possible answer: All admins are staff
        return self.is_admin
