from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "menus"

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=30)
    english_name = models.CharField(max_length=30)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 5, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 5, decimal_places = 2)
    saturated_fat_g = models.DecimalField(max_digits = 10, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 5, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 5, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 5, decimal_places = 2)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length=500)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
 
    class Meta:
        db_table = 'imagess'

class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergy'

class Allergy_product(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_products"
