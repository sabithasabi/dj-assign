from django.db import models

# Create your models here.
class Signup(models.Model):
    First_name=models.TextField()
    Last_name=models.TextField()
    profile_picture=models.ImageField()
    username=models.TextField()
    email_id=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)
    address=models.CharField(max_length=20)
    line1=models.CharField(max_length=20)
    city=models.TextField()
    state=models.TextField()
    pincode=models.IntegerField()
    def __str__(self):
        return self.name

class Signup2(models.Model):
    First_name=models.TextField()
    Last_name=models.TextField()
    profile_picture=models.ImageField()
    username=models.TextField()
    email_id=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)
    address=models.CharField(max_length=20)
    line1=models.CharField(max_length=20)
    city=models.TextField()
    state=models.TextField()
    pincode=models.IntegerField()
    def __str__(self):
        return self.name