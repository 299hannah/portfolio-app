from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class About(models.Model):
    description=models.TextField()
    image = CloudinaryField('image')
    class Meta:
        verbose_name="About me"
        verbose_name_plural = "About me"
    
    def __str__(self):
        return "About me"

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Service name")
    description=models.TextField(verbose_name="About service")
    # image = CloudinaryField('image')



    def __str__(self):
        return self.name


class Projects(models.Model):
    title=models.CharField(max_length=255, null=True, verbose_name="Project title")
    image = CloudinaryField('image')
    url =models.CharField(max_length=255, null=True)
    body = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title


