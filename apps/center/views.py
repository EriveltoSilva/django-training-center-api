from apps.center import models
from rest_framework import viewsets
from apps.center import serializers
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class UserViewset(viewsets.ModelViewSet):
    ''' Show all users '''
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentViewset(viewsets.ModelViewSet):
    ''' Show all Students '''
    queryset= models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TeacherViewset(viewsets.ModelViewSet):
    ''' Show all Teachers '''
    queryset= models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseViewset(viewsets.ModelViewSet):
    ''' Show all Courses '''
    queryset = models.Course.objects.all()
    serializer_class= serializers.CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes  = [IsAuthenticated]

class RoomViewset(viewsets.ModelViewSet):
    ''' Show all Rooms '''
    queryset = models.Room.objects.all()
    serializer_class= serializers.RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class ClassRoomViewset(viewsets.ModelViewSet):
#     ''' Show all ClassRooms '''
#     queryset = models.ClassRoom.objects.all()
#     serializer_class= serializers.ClassRoomSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

class OnlyListClassRoomViewset(ListAPIView):
    ''' Show all ClassRooms '''
    def get_queryset(self):
        return models.ClassRoom.objects.filter(course_id=self.kwargs['pk']) 
    serializer_class= serializers.OnlyListClassRoomsSerializer

class RegistrationViewset(viewsets.ModelViewSet):
    ''' Show all Registrations '''
    queryset = models.Registration.objects.all()
    serializer_class= serializers.RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class NoteViewset(viewsets.ModelViewSet):
    ''' Show all Notes '''
    queryset = models.Note.objects.all()
    serializer_class= serializers.NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
