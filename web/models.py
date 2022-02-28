
from django.db import models

# Create your models here.
class Subscribe(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email


class Customer(models.Model):
    image=models.FileField(upload_to="customers")


    def __str__(self):
        return str(self.image)
class Feature(models.Model):
    image=models.ImageField(upload_to="feature/image")
    icon=models.FileField(upload_to="feature/icon")
    icon_background=models.CharField(max_length=225)
    title=models.CharField(max_length=225)
    description=models.TextField()
    testimonial_description=models.TextField()
    testimonial_author=models.CharField(max_length=225)
    auther_desigination=models.CharField(max_length=225)
    testimonial_logo=models.FileField(upload_to="feature/testimonial_logo")

    def __str__(self):
        return str(self.image)
