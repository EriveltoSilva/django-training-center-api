from rest_framework import serializers
from apps.center import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','last_name','email']
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'user','bi',
                  'birthday','gender','race',
                  'civil_status','natianality']
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'user','bi',
                  'birthday','gender','race',
                  'civil_status','nationality','formation_area',
                  'formation_title']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','code','description','duraction',
                  'duraction_unit',]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','name','number',]

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassRoom
        fields = ['id','course','teacher',
                  'room','status','time_start',
                  'time_end']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = ['id','class_room','student',
                  'data',]

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['id','teacher','class_room',
                  'student','value','unit']