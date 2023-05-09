from django.db import models

# Create your models here.
# class Employee(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=30)
#     phone = models.CharField(max_length=10)

class ToDo(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField(max_length=30)
    Date = models.DateField(max_length=30)
    Completed = models.BooleanField(max_length=10)

    def __str__(self):
        return self.Title

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
   
