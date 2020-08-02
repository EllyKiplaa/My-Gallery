from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return self.location_name


    def save_location(self):
        self.save()
class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.cat_name


    def save_category(self):
        self.save()
