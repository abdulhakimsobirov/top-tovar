from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_images/",  null=True, blank=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to="product_images/",  null=True, blank=True)
    video = models.FileField(upload_to="product_videos/",  null=True, blank=True)
    top = models.BooleanField()

    def __str__(self):
        return self.name


class Request(models.Model):
    REGION = (
        ('Toshkent shahar', 'Toshkent shahar'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Andijon', 'Andijon'),
        ('Buxoro', 'Buxoro'),
        ('Fargona', 'Fargona'),
        ('Jizzax', 'Jizzax'),
        ('Namangan', 'Namangan'),
        ('Navoiy', 'Navoiy'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Qoraqalpogiston', 'Qoraqalpogiston'),
        ('Samarqand', 'Samarqand'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Surxandaryo', 'Surxandaryo'),
        ('Xorazm', 'Xorazm'),
    )

    client_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    region = models.CharField(max_length=50, choices=REGION)

    def __str__(self):
        return self.client_name
