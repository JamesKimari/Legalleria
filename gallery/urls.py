from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.gallery, name = 'gallery'),
    path('search/', views.search_results, name = 'search_results'),
    path('categories/', views.display_images_categories, name = 'categories'),
    path('locations/', views.display_images_locations, name = 'locations'),
    path('image/<int:image_id>', views.single_pic, name = 'single_pic')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)