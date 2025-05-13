from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Myapp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    word_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.name}"
    
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"