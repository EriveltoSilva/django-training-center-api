from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',views.UserViewset, basename="users")
router.register('students', views.StudentViewset, basename="students")
router.register('teachers', views.TeacherViewset, basename="teachers")
router.register('courses',views.CourseViewset, basename="courses")

urlpatterns = [
    path('', include(router.urls)),
]