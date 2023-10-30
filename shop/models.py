from django.db import models

<<<<<<< HEAD

class Product(models.Model):
    SIZES = [
        ("S", "S"),
        ("SM", "SM"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]
    DEFAULT_SIZES = 'L'

    manufacturer = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sales = models.PositiveSmallIntegerField()
    size = models.CharField(
        choices=SIZES,
        max_length=3,
        default=DEFAULT_SIZES,
    )
    type = models.PositiveSmallIntegerField()
    description = models.TextField()
    details = models.JSONField()
    rating = models.FloatField()
    slug = models.SlugField()


class Category(models.Model):
    pass


class Comment(models.Model):
    GRADES = [
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Not bad'),
        (2, 'Badly'),
        (1, 'Terrible'),
    ]
    DEFAULT_GRADE = 5

    client = models.ForeignKey('account.Client', on_delete=models.CASCADE)
    text = models.TextField()
    grade = models.CharField(
        max_length=16,
        choices=GRADES,
        default=DEFAULT_GRADE
    )
=======
# Create your models here.
>>>>>>> develop
