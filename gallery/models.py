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
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_path = models.ImageField(upload_to = 'gallery/')
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(image_category__cat_name__icontains=search_term)
        return search_result

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()