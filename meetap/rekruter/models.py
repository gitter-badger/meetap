from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from meetap.settings import AUTH_USER_MODEL
import uuid


# Klasa zmienia autentykację Usera na email jak w Core2.
class User(AbstractBaseUser, PermissionsMixin):
    USER = 1
    COUNCIL = 2
    COUNCIL_ADMIN = 3
    SUPERUSER = 4
    ROLE_CHOICES = (
     (USER, 'User'),
     (COUNCIL, 'Council'),
     (COUNCIL_ADMIN, 'Council Admin'),
     (SUPERUSER, 'Superuser'),
    )
    OTHER = 0
    MALE = 1
    FEMALE = 2
    GENDERS = (
     (OTHER, 'other'),
     (MALE, 'male'),
     (FEMALE, 'female'),
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True)
    is_translator = models.BooleanField(_('translator'), default=False)
    is_hotel = models.BooleanField(_('hotel'), default=False)
    role_council = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True, default=1)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    quarter = models.CharField(_('quarter'), max_length=2, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS, null=True, blank=True)
    citizenship = models.CharField(_('citizenship'), max_length=40, blank=True)
    dowod = models.CharField(_('dowod'), max_length=20, blank=True)
    passport = models.CharField(_('passport'), max_length=20, blank=True)
    telephone = models.CharField(_('telephone'), max_length=20, blank=True)
    street = models.CharField(_('street'), max_length=30, blank=True)
    building_no = models.CharField(_('building_no'), max_length=15, blank=True)
    local_no = models.CharField(_('local_no'), max_length=10, blank=True)
    postcode = models.CharField(_('postcode'), max_length=7, blank=True)
    city = models.CharField(_('city'), max_length=25, blank=True)
    album = models.CharField(_('album'), max_length=25, blank=True)
    language = models.CharField(_('album'), max_length=2, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
