from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class CategoryTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.design=Category(name='Design')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.design,Category))

    #Testing Save Method
    def test_save_method(self):
        self.design.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_method(self):



        self.design.save_category()
        self.design.delete_category()

class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.nairobi=Location(name='Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    #Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        '''
        Function that tests whether a location can be deleted
        '''
        self.nairobi.save_location()
        self.nairobi.delete_location()


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new category and saving it
        self.new_category= Category(name = 'Design')
        self.new_category.save_category()

        # Creating a new location and saving it
        self.new_location= Location(name = 'Nairobi')
        self.new_location.save_location()

        self.new_image= Image(image='image.jpeg',name = 'Test Image',description = 'This is a random test Image description',category = self.new_category,location=self.new_location)
        self.new_image.save()

        # self.new_image.category.add(self.new_category)
        # self.new_image.category.add(self.new_location)


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()