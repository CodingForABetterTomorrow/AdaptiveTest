from django.db import models


# Create your models here.
class Test(models.Model):
    TestID=models.CharField(max_length=10)
    passwd = models.CharField(max_length=10)
    description=models.TextField()
    Company = models.CharField(max_length=40)
    math=models.IntegerField(default=0)
    lr=models.IntegerField(default=0)
    eng=models.IntegerField(default=0)
    def __str__(self):
        return self.TestID


class Question(models.Model):
    ques = models.CharField(max_length=255)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    rightAns =  models.CharField(max_length=1)
    diff = models.CharField(max_length=10)
    field =  models.CharField(max_length=10)
    origin =  models.CharField(max_length=10)
    def __str__(self):
        return self.ques
