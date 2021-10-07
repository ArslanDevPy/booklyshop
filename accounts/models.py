from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager
from django.utils.html import format_html
from BookShop.utils import admin_img


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255)
    objects = UserManager()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'user'
        verbose_name = _(" User")
        verbose_name_plural = _(" Users")

    @property
    def profile_img(self):
        return admin_img(self.profile.img.url)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='accounts/profile/', default='accounts/profile/profile.png')

    def __str__(self):
        return self.user.name

    class Meta:
        db_table = "profile"
        verbose_name = _(' Profile')
        verbose_name_plural = _(" Profile")

    @property
    def profile_img(self):
        return self.user.profile_img

    @property
    def full_name(self):
        if not self.first_name or self.last_name:
            return "unknown"
        return f"{self.first_name} {self.last_name}"

    @property
    def user_email(self):
        return self.user.email

    @property
    def user_last_login(self):
        return self.user.last_login

    @property
    def user_join(self):
        return self.user.date_joined


class UserAddress(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zipCode = models.CharField(max_length=10)
    city = models.CharField(max_length=60)
    State = models.CharField(max_length=60)
    status = models.BooleanField(default=True)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True,editable=False)
    update_at = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.user.name + self.title

    class Meta:
        db_table = "userAddress"
        verbose_name = _(' User Address')
        verbose_name_plural = _(" Users Address")
