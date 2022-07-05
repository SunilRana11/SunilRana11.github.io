from django.db import models
from datetime import datetime,date


# Create your models here.


class Teacher(models.Model):
    TEACHES = {
        ('primary','primary'),
        ('secondary','secondary'),
    }
    image = models.ImageField(default = '',upload_to = '')
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    joined_date = models.DateField(auto_now=False,auto_now_add=False)
    contact = models.CharField(max_length=20)
    teaches = models.CharField(max_length=30,choices=TEACHES,default='primary')
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Student(models.Model):
    STANDARD = (
        (1,"I"),
        (2,"II"),
        (3,"III"),
        (4,"IV"),
        (5,'V'),
        (6,'VI'),
        (7,'VII'),
        (8,'VIII'),
        (9,'IX'),
        (10,'X'),
    )
    image = models.ImageField(default = '',upload_to = '')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    parentsContact = models.CharField(max_length=20)
    standard = models.IntegerField(choices=STANDARD)
    status = models.BooleanField(default=False)
    


    def __str__(self):
        return self.name




class Result(models.Model):

    image = models.ImageField(default = '',upload_to = '')
    
    batch = models.DateField(auto_now=False,auto_now_add=False)

    title = models.CharField(max_length=300,default = '')


    standard = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.title




class Notice(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(max_length=1000)

    image = models.ImageField(default = '',upload_to = '')


    def __str__(self):
        return self.title



        



    

