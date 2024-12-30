from django.db import models
# PermissionsMixin ব্যবহার করার কারণ:
# 1. এটি Django এর built-in পারমিশন সিস্টেম ব্যবহার করতে সাহায্য করে
# 2. ইউজার গ্রুপ এবং পারমিশন ম্যানেজ করার জন্য প্রয়োজনীয় ফিল্ড এবং মেথড প্রদান করে
# 3. কাস্টম ইউজার মডেল তৈরি করার সময় এটি ব্যবহার করা বাধ্যতামূলক
# 4. এটি ইউজার অথেনটিকেশন এবং অথরাইজেশন সিস্টেম implement করতে সাহায্য করে
from django.contrib.auth.models import PermissionsMixin
# AbstractBaseUser ব্যবহার করার কারণ:
# 1. কাস্টম ইউজার মডেল তৈরি করার জন্য এটি ব্যবহার করা হয়
# 2. এটি ইউজার অথেনটিকেশন এর জন্য প্রয়োজনীয় ফিল্ড এবং মেথড প্রদান করে
# 3. এটি ইউজার মডেল কে customize করার সুযোগ দেয়
from django.contrib.auth.base_user import AbstractBaseUser
# UnicodeUsernameValidator ব্যবহার করার কারণ:
# 1. এটি ইউজারনেম ভ্যালিডেশনের জন্য ব্যবহৃত হয়
# 2. এটি নিশ্চিত করে যে ইউজারনেম শুধুমাত্র Unicode ক্যারেক্টার ধারণ করে
# 3. এটি @ . + - _ যেমন স্পেশাল ক্যারেক্টার সাপোর্ট করে
# 4. এটি Django এর built-in ভ্যালিডেটর
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser,PermissionsMixin):
    """Model definition for User."""

    # TODO: Define fields here
    username = models.CharField(max_length=150, validators=[UnicodeUsernameValidator(), ], unique=True )
    email = models.EmailField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    # _("") হলো Django এর internationalization/translation সিস্টেমের একটি ফাংশন
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # objects হলো Django এর model manager
    # এটি ডাটাবেস অপারেশন যেমন create, filter, update ইত্যাদি করার জন্য ব্যবহৃত হয়
    # None এর পরিবর্তে UserManager() ব্যবহার করা উচিত
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]
    class Meta:
        """Meta definition for User."""
        # ইউজারদের সাজানো হবে সর্বশেষ যোগদানকৃত থেকে প্রথম যোগদানকৃত পর্যন্ত, কারণ date_joined একটি টাইমস্ট্যাম্প
        ordering = ['-date_joined'] 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username