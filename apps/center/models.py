from django.db import models
from django.contrib.auth.models import User
# Create your models here

GENDER=(('M','MALE'), ('F', 'FEMALE'))
RACE=(('B','BLACK'), ('W', 'WHITE'))
CIVIL_STATUS=(('S','SINGLE'), ('M', 'MARRIED'),('D','DIVORCED'),('W','WIDOWER'))
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bi = models.CharField(max_length=14, null=False, blank=False, unique=True)
    birthday = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    race = models.CharField(max_length=1, choices=RACE, default='B')
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS, default='S')
    natianality = models.CharField(max_length=100, null=False, blank=False)     
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    

    def get_full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    
class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bi = models.CharField(max_length=14, null=False, blank=False, unique=True)
    birthday = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    race = models.CharField(max_length=1, choices=RACE, default='B')
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS, default='S')
    nationality = models.CharField(max_length=100, null=False, blank=False)
    formation_area = models.CharField(max_length=100, null=False, blank=False)  
    formation_title = models.CharField(max_length=100, null=False, blank=False)   
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    

    def get_full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
    def __str__(self) -> str:
        return self.get_full_name()
    

class Course(models.Model):
    DURACTION_UNIT = (('D','DAYS'),('W','WEEKS'),('M','MONTHS'),('Y','YEARS'),)
    code = models.CharField(max_length=10, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255,null=False, blank=False)
    duraction = models.IntegerField(null=False, blank=False)
    duraction_unit = models.CharField(max_length=10,choices=DURACTION_UNIT,default="M",null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return f"{self.description}"


class Room(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    number = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class ClassRoom(models.Model):
    STATUS = (('MARKED','MARKED'),('STARTED','STARTED'),('FINISHED','FINISHED'))
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
    time_start = models.TimeField()
    time_end = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.course.code} - {self.course.description}"
    
    def period(self) -> str:
        return f"---PERIOD NOT SET---"


class Registration(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    data= models.DateField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f"{self.student}- {self.class_room}"
    

class Note(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom,on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, null=False)
    value =  models.IntegerField(default=0)
    unit = models.CharField(max_length=10, default="")

    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now_add=True)
