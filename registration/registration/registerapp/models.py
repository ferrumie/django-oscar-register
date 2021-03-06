from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _  # translation hook


class UserManager(BaseUserManager):
    """
    Override Base Django Manager model to make
    email the default for authentication
    instead of username
    """
    use_in_migrations = True

    def icreate_user(self, email, first_name, last_name, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, 
                    last_name, password=None, **extra_fields):
        """
        create user custom
        """
        extra_fields.setdefault('is_superuser', False)
        return self.icreate_user(email, password,
                                 first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.icreate_user(email, password, first_name, last_name, **extra_fields)


class RegisterUser(AbstractBaseUser):
    """
    Register user model, Extending Django user model

    """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
    
    def __str__(self):
        return self.email
