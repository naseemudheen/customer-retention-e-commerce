from email.quoprimime import unquote
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyUserManager(BaseUserManager):
    def create_user(self,email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),        
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10, null=False, blank=False)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, 
    )
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = MyUserManager()


    def __str__(self):
        return str(self.name)

    def has_perm(self,perm,obj=None):
        return self.is_admin
        
    def has_module_perms(self,app_label):
        return True
    

    def get_all_permissions(self):
        return True
    