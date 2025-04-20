from django.db import models

# Create your models here.

class User(models.Model):
    Name=models.CharField(max_length=20, default='')
    Mail=models.CharField(default='')
    Address=models.CharField(max_length=30, default='')
    Mobile=models.BigIntegerField (default=0)
    Password=models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.Name} ({self.Mail})'
    