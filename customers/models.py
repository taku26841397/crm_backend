from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Customer(models.Model):
    
    
    
    STATUS_CHOICES = [
        ("new", "新規"),
        ("in_progress", "対応中"),
        ("closed", "成約"),
    ]
    
    name = models.CharField(max_length=100)
    
    company = models.CharField(max_length=100,blank=True)
    
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="new")
    
    email = models.EmailField(blank=True)
    
    address = models.CharField(max_length=125,blank=True)
    
    phone = models.CharField(
        max_length=25,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9\-]+$',
                message="電話番号は数字とハイフンのみ入力できます"
            )
        ])
    
    memo = models.TextField(blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    next_action = models.CharField(max_length=255,default="",blank=True)
    
    next_action_date = models.DateField(null=True,blank=True)
    
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customers',
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.name
    

class Activity(models.Model):
    
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,
        related_name="activities"
        )
    
    activity_type = models.CharField(max_length=50)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.customer.name} - {self.activity_type}"
    

class Profile(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    image = models.ImageField(
        upload_to = "profile/",
        blank =True,
        null = True,
    )
    def __str__(self):
        return f"{self.user}のプロフィール"

# Create your models here.
