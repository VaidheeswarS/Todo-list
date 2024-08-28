from django.db import models

# Create your models here.

class User_Registration(models.Model):
    S_No=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=20,null=True)
    Email=models.EmailField(max_length=100,null=True)
    Phonenumber=models.BigIntegerField(null=True)
    Age=models.IntegerField(null=True)
    Password=models.TextField(max_length=10,null=True)

class Login_data(models.Model):
    S_No=models.AutoField(primary_key=True)
    email_id=models.EmailField(max_length=100,null=True)
    password=models.TextField(max_length=10,null=True)


class Works(models.Model):
    No=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=100,null=True)
    work=models.TextField(max_length=10000,null=True)
    Created_on=models.TimeField(auto_now_add=True)
    updated_on=models.TimeField(auto_now=True)
    Submit_time=models.DateField(null=True)
    status=models.CharField(max_length=10,null=True)
    To=models.ForeignKey("Login_data",on_delete=models.CASCADE)
    