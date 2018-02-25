from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.blackpanther = Image(name = 'blackpanther', description = 'a black panther poster')
        self.blackpanther.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.blackpanther, Image))

    def test_save_method(self):
        self.blackpanther.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)            

    def test_delete_method(self):
        self.new_image = Image(name = 'intercontinental', description = 'a birds eye view of the Intercontinental hotel')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

    def test_update_method(self):
        self.Elaine = Image(name = 'Elaine', description = 'she is an attractive lady')
        self.Elaine.save_image()
        self.Elaine = Image(name = 'Elena', description = 'she is an attractive lady')        
        self.Elaine.update_image(name = 'Elena')
        self.Elaine.save_image()
        images = Image.objects.filter(name = 'Elena')
        pics = Image.objects.all()
        # print(images)
        # print(pics)        
        self.assertEqual(len(images), 1)

class LocationTestClass(TestCase):    
    def setUp(self):
        self.Kenya = Location(name = 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, Location))

    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location = Location(name = 'Kiambu')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

    def test_update_method(self):
        self.Nairobi = Location(name = 'Nairobi')
        self.Nairobi.save_location()
        self.Nairobi = Location(name = 'Nai')
        self.Nairobi.save_location()
        self.Nairobi.update_location(name = 'Nai')
        locations = Location.objects.filter(name = 'Nai')
        self.assertEqual(len(locations), 1)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Selfies = Category(name = 'selfies')

    def test_instance(self):
        self.assertTrue(isinstance(self.Selfies, Category))

    def test_save_method(self):
        self.Selfies.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.new_category = Category(name = 'Siberian Huskies')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_category(self):
        self.health = Category(name = 'Health')
        self.health.save_category()
        self.health = Category(name = 'medicine')
        self.health.save_category()
        self.health.update_category(name = 'medicine')
        categories = Category.objects.filter(name = 'medicine')
        self.assertEqual(len(categories), 1)