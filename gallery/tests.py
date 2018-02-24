from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.blackpanther = Image(name = 'blackpanther', description = 'a black panther poster')

    def test_instance(self):
        self.assertTrue(isinstance(self.blackpanther, Image))

    def test_save_method(self):
        self.blackpanther.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.Kenya = Location(name = 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, Location))

    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Selfies = Category(name = 'selfies')

    def test_instance(self):
        self.assertTrue(isinstance(self.Selfies, Category))

    def test_save_method(self):
        self.Selfies.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)