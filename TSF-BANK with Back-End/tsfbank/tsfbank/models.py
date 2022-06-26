from django.db import models

class addcustomer(models.Model):
    regid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    account=models.CharField(max_length=10)
    balance=models.CharField(max_length=1000)
    role=models.CharField(max_length=10)
    dt=models.CharField(max_length=1000)

class trans(models.Model):
    regid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    sacc=models.CharField(max_length=60)
    sb=models.CharField(max_length=15)
    rname=models.CharField(max_length=30)
    amount=models.CharField(max_length=20)
    dt=models.CharField(max_length=1000)