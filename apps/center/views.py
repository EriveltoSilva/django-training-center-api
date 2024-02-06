from rest_framework import viewsets
from apps.center import models
from apps.center import serializers
from django.contrib.auth.models import User


class UserViewset(viewsets.ModelViewSet):
    ''' Show all users '''
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class StudentViewset(viewsets.ModelViewSet):
    ''' Show all Students '''
    queryset= models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class TeacherViewset(viewsets.ModelViewSet):
    ''' Show all Teachers '''
    queryset= models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class CourseViewset(viewsets.ModelViewSet):
    ''' Show all Courses '''
    queryset = models.Course.objects.all()
    serializer_class= serializers.CourseSerializer