from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)        

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=20)    

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['name']

  


