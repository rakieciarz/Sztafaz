from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Model of product's
class Index(models.Model):
    # Selection list for Country
    class Country(models.TextChoices):
        PL = 'Poland'
        CZ = 'Czech Republic'
        CS = 'Czechoslovakia'
        DE = 'Germany'
        FR = 'France'
        BG = 'Belgium'
        IT = 'Italy'
        DN = 'Denmark'
        SE = 'Sweden'

    # Selection list for Category
    class Category(models.TextChoices):
        FURNITURE = 'Furniture'

    # Selection list for Subcategory
    class Subcategory(models.TextChoices):
        CHAIR = 'Chair'

    # Selection list for Material
    class Material(models.TextChoices):
        WOOD = 'Wood'

    item_ID = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    descriptions = models.TextField(blank=True)

    category = models.CharField(max_length=64, choices=Category.choices)
    subcategory = models.CharField(max_length=64, choices=Subcategory.choices)
    material = models.CharField(max_length=32, choices=Material.choices)
    country = models.CharField(max_length=32, choices=Country.choices)

    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    PKWIU = models.CharField(max_length=32, blank=True)

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Models for inventory and details od product
class Product(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    purchase_cost = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=32)

    def __str__(self):
        return self.index.name


# Model that collect images
class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_first = models.BooleanField(default=False)
    images = models.ImageField(upload_to='ERP/media/')

    def __str__(self):
        return self.product.name


# Models for suppliers and vendors
class Vendors(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=16, blank=True)
    contact_person = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


# Model for registered orders
class OrderHeader(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'Cash'
        CARD = 'Card'
        FREE = 'Free of expense'

    order_number = models.CharField(max_length=16)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=16, choices=PaymentMethod.choices)
    is_paid = models.BooleanField(default=False)
    cost = models.IntegerField(default=0)
    other_expenses = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
    purchase_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number


# Model for details of HeaderOrder
class OrderDetails(models.Model):
    order_number = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)  # It will be ForeignKey
    quantity = models.IntegerField(max_length=16)
    cost = models.IntegerField(default=0)
    other_expenses = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.order_number.name

