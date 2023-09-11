from django.db import models

# Create your models here.
class adminDatabase(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)


class userDatabase(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)


class queryDatabase(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Query=models.CharField(max_length=300)
