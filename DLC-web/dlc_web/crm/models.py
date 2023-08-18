from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

COUNTRIES = (
    ("LT", _("Lithuanian")),
    ("EN", _("English")),
    ("RU", _("Russian")),
    ("PL", _("Poland")),
)


class Category(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "name = {}".format(self.name)


class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    communication = models.CharField(max_length=2, choices=COUNTRIES)
    comment = models.CharField(max_length=1000)
    activity = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return "{}, country = {}".format(self.customer_name, self.communication)


class Event(models.Model):
    comment = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Event by: {} customer: {} time: {}".format(self.user, self.customer, self.created)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return "Product name = {}".format(self.product_name)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.name)


class Work_list(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return "Name = {}".format(self.name)


class News_list(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return "Name = {}".format(self.name)



x = ['abecele', 'bubu', 'emilija', 5]

for i in x:
    if i == str():
        print("tai yra raide")
    else:
        print("tai yra skaicius")