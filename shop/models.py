from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.contrib.auth import get_user_model
from accounts.models import UserAddress
import random
import string
from django.utils import timezone
from BookShop.utils import auto_slug, admin_img


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


User = get_user_model()


class BaseModel(models.Model):
    slug = models.SlugField(max_length=300, primary_key=True, unique=True)
    create_at = models.DateTimeField(auto_now=timezone.now(), null=True, blank=True)
    update_at = models.DateTimeField(auto_now=timezone.now(), null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = auto_slug(Category, self.title, self.slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "category"
        verbose_name = _(' Category')
        verbose_name_plural = _(" Categories")


class Author(BaseModel):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to='shop/book/author/', default='shop/book/author/author.png')
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = auto_slug(Author, self.title, self.slug)
        return super().save(*args, **kwargs)

    def author_image(self):
        return admin_img(self.img.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "author"
        verbose_name = _(' Author')
        verbose_name_plural = _(" Authors")


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Book(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    ISBN = models.CharField(max_length=30)
    year = models.CharField(max_length=10, default=datetime.datetime.now().year)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0, null=True)
    noPage = models.IntegerField(default=0)
    description = models.TextField()
    tag = models.ManyToManyField(to=Tag,related_name='tag_rel')
    img = models.ImageField(upload_to='shop/book/', default='shop/book/book.png')

    def save(self, *args, **kwargs):
        self.slug = auto_slug(Book, self.title, self.slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -- {self.author.title}"

    def get_tag(self):
        return self.tag

    def get_sale_price(self):
        return float(self.price)-float(self.discount)

    class Meta:
        db_table = "book"
        verbose_name = _(' Book')
        verbose_name_plural = _(" Books")


class OrderDetails(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.book.title} -- {self.book.author.title}"

    class Meta:
        db_table = "orderdetails"
        verbose_name = _(' Order Detail')
        verbose_name_plural = _(" Orders Details")


class Order(models.Model):
    Processing = "Processing"
    ON_HOLD = "On Hold"
    Completed = "Completed"
    Cancelled = "Cancelled"
    Refunded = "Refunded"
    Failed = "Failed"
    choices = ((Processing, Processing), (ON_HOLD, ON_HOLD), (Completed, Completed),
               (Cancelled, Cancelled), (Refunded, Refunded), (Failed, Failed))
    OrderDetail = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    status = models.CharField(max_length=30, choices=choices)
    date = models.DateTimeField(auto_created=True, editable=False)

    def __str__(self):
        return f"{self.customer} - {self.price}"

    class Meta:
        db_table = "Order"
        verbose_name = _(' Order')
        verbose_name_plural = _(" Orders")
