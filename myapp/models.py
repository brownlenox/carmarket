import os.path
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def unique_image_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    # full_name = "%s.%s" % (name, ext)
    return os.path.join('cars', full_name)

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(default='null')
    seller_phone = models.CharField(max_length=15, default='+2547...')
    model = models.IntegerField()
    image = models.ImageField(upload_to=unique_image_name, blank=True, null=True)
    price = models.CharField(max_length=50, default='free')
    car_type = models.CharField(max_length=50, default='null')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cars'
