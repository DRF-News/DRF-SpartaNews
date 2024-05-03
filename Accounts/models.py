from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    objects = CustomUserManager()
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=30,
        unique=True,
        help_text=(
            "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    email = models.EmailField(unique=True, blank=True)
    intro = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []