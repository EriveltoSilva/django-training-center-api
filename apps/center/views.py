from rest_framework import viewsets
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    """Show all Students """
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewset(viewsets.ModelViewSet):
    """ Show all Courses """
    queryset = Course.objects.all()
    serializer_class= CourseSerializer