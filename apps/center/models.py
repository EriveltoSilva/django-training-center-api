from django.db import models

# Create your models here
class Student(models.Model):
    name = models.CharField(max_length=100)
    bi = models.CharField(max_length=14)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self) -> str:
        return f"{self.name}"
    
class Course(models.Model):
    LEVELS = (('SS', 'LEGEND'), 
              ('S',  'START'),
              ('A',  'ADVANCED'),
              ('B',  'ALMOST-ADVANCED'),
              ('C',  'INTERMEDIATE'),
              ('D',  'PRE-INTERMEDIATE'),
              ('E',  'BASIC'))
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    level = models.CharField(max_length=10,choices=LEVELS, default='E',blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return f"{self.description}"