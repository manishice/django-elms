from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class admin_table(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    uname = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    creation_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.fullname
    
class department(models.Model):
    title = models.CharField(max_length=100)
    shortform = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
class employee(models.Model):
    eid = models.CharField(max_length=100)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    regdate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.fname
    
    
class leave_type(models.Model):
    
    leavetype = models.CharField(max_length=100)
    description = models.TextField()
    createdAt = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.leavetype
    
class leave(models.Model):
    leavetype= models.CharField(max_length=100)
    toDate=models.DateField()
    fromDate = models.DateField()
    description = models.TextField()
    request_date = models.DateTimeField(default=timezone.now)
    adminRemark= models.TextField()
    adminRemarkDate = models.CharField(max_length=255)
    status = models.IntegerField()
    isRead = models.IntegerField()
    eid = models.ForeignKey(employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.leavetype
    