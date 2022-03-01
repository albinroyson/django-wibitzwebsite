
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


class Video(models.Model):
    image=models.ImageField(upload_to="video/image")
    icon=models.FileField(upload_to="video/icon")
    title=models.CharField(max_length=225)

    def __str__(self):
        return str(self.image)


class Profile(models.Model):
    image=models.ImageField(upload_to="video/image")
    icon=models.FileField(upload_to="video/icon")
    discribe =models.CharField(max_length=225)
    name =models.CharField(max_length=225)
    desigination=models.CharField(max_length=225)
    company=models.CharField(max_length=225)

    def __str__(self):
        return str(self.image)


class Marketing(models.Model):
    image=models.FileField(upload_to="market/image")
    title =models.CharField(max_length=225)
    discribe =models.CharField(max_length=225)

    def __str__(self):
        return str(self.image)

class Studio(models.Model):
    icon=models.FileField(upload_to="studio/icon")
    image=models.FileField(upload_to="studio/image")
    title =models.CharField(max_length=225)
    discribe =models.CharField(max_length=225)

    def __str__(self):
        return str(self.image)



class Blog(models.Model):

    image=models.FileField(upload_to="blog/image")
    discribe =models.CharField(max_length=225)

    def __str__(self):
        return str(self.image)
