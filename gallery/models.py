from django.db import models

# Create your models here.
CATEGORIES = (
    ('Illustrations', 'Illustrations'),
    ('Interior', 'Interior'),
    ('Random', 'Random'),
    ('Siberian', 'Siberian'),
    ('Wakanda', 'Wakanda'),
)

class Category(models.Model):
    name = models.CharField(max_length=15, choices=CATEGORIES)        

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()    

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()

    @classmethod
    def update_category(cls, id, category, update):
        updated = cls.objects.filter(id=id).update(category=update)
        return updated

LOCATIONS = (
    ('Poka Universe', 'Poka Universe'),
    ('Singapore', 'Singapore'),
    ('Nairobi, Kenya', 'Nairobi, Kenya'),
    ('Siberia', 'Siberia'),
    ('Wakanda', 'Wakanda'),
)

class Location(models.Model):
    name = models.CharField(max_length=20, choices=LOCATIONS)    

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    

    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()

    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id=id).update(location=update)
        return updated


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

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 

    @classmethod
    def update_image(cls, id, pic, update):
        updated = cls.objects.filter(id=id).update(pic=update) 
        return updated 

    @classmethod
    def display_all_pics(cls):
        pics = cls.objects.all()
        return pics 

    @classmethod
    def get_pic(cls, id):
        pic = cls.objects.get(id=id)
        return pic

    @classmethod
    def filter_by_location(cls):
        pics = cls.objects.filter(location__in=locations)

    class Meta:
        ordering = ['name']

    

  


