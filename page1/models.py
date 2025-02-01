from django.db import models
from django.contrib import admin

class emp(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    class Meta:
        db_table = 'employee'
        verbose_name = "emp_info"
        

class users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'login_info'
        verbose_name = "users_info"
    
         
# Create your models here.
