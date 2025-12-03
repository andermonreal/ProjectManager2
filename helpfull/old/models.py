from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, name, email, password, phone, birthday, **extra_fields):
        if not email:
            raise ValueError("Email is mandatory")
        if not password:
            raise ValueError("Password is required")
        if User.is_older_than(birthday, 18) is False:
            raise ValueError("The user must be of legal age")
        
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault('is_active', True)

        user = self.model(name=name, email=email, phone=phone, birthday=birthday, **extra_fields)
        user.set_password(password)  # hashea el password
        user.save(using=self._db)

        print(f"Usuario creado en el manager {user}")
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    class Meta:
        db_table = 'users'

    objects = UserManager()

    @staticmethod
    def is_older_than(birthday, age='18'):
        today = timezone.now().date()
        age_difference = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        return age_difference >= age
    
    def __str__(self):
        return self.email
