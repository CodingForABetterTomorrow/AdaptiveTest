from django.db import models

# Create your models here.
class Student(models.Model):
	testid = models.CharField(max_length=255)
	testpassword = models.CharField(max_length=255)
	studentname = models.CharField(max_length=255)
	studentemail = models.EmailField(max_length=255)
	marks=models.IntegerField(default=-1)
	totalmarks=models.IntegerField(default=-1)

