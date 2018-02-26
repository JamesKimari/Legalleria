from django.db import models

# Create your models here.
CATEGORIES = (
    ('1', 'Illustrations'),
    ('2', 'Interior'),
    ('3', 'Random'),
    ('4', 'Siberian'),
    ('5', 'Wakanda'),
)

class Category(models.Model):
    name = models.CharField(max_length=1, choices=CATEGORIES)        

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def update_category(self, **kwargs):
        Category.objects.filter(id = self.pk).update(**kwargs)

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()

LOCATIONS = (
    ('1', 'Poka Universe'),
    ('2', 'Singapore'),
    ('3', 'Nairobi, Kenya'),
    ('4', 'Siberia'),
    ('5', 'Wakanda'),
)

class Location(models.Model):
    name = models.CharField(max_length=1, choices=LOCATIONS)    

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def update_location(self, **kwargs):
        Location.objects.filter(id = self.pk).update(**kwargs)

    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()

class Image(models.Model):
    image = models.ImageField(upload_to = '', null = True, blank = True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def update_image(self, **kwargs):
        name = Image.name
        Image.objects.filter(id = self.pk).update(**kwargs)

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()   

    @classmethod
    def display_all_pics(cls):
        pics = cls.objects.all()
        return pics 

    class Meta:
        ordering = ['name']

    

  


