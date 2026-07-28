from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone= models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name