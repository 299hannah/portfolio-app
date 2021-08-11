from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.
class About(models.Model):
    description=models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name="About me"
        verbose_name_plural = "About me"
    
    def __str__(self):
        return "About me"

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Service name")
    description=models.TextField(verbose_name="About service")


    def __str__(self):
        return self.name


class Projects(models.Model):
    title=models.CharField(max_length=255, null=True, verbose_name="Project title")
    image=models.ImageField(upload_to="work", blank=True)
    body = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

# class Client(models.Model):
#     name=models.CharField(max_length = 255)
#     description = models.TextField(verbose_name="client say")
#     image = models.ImageField(upload_to="clients",default="default.png")

#     def __str__(self):
#         return self.name
     

