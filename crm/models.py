from django.db import models

class Employees(models.Model):

    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    contact=models.CharField(null=True,max_length=200)
    profile_pic=models.ImageField(upload_to="image",null=True)

    def __str__(self) :
        return self.name

