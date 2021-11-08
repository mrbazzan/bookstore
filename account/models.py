
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, name, email, date_of_birth, password=None):
        if not name:
            raise ValueError("Users must have a name")
        if not email:
            raise ValueError('Users must have an email address')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, date_of_birth, password=None):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_kid = models.BooleanField(default=False)
    name = models.CharField(max_length=255, unique=True)
    profile = models.FileField(max_length=255)
    AGE_RANGE = [('18+', 'Adult'), ('<18', 'Adolescent')]
    age = models.CharField(max_length=3, choices=AGE_RANGE)
    created_at = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


@receiver(post_save, sender=User)
def update_is_kid(sender, instance, **kwargs):
    if instance.is_admin is False and instance.age == '<18':
        sender.objects.filter(pk=instance.pk).update(is_kid=True)
