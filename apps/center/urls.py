from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',views.UserViewset, basename="users")
router.register('students', views.StudentViewset, basename="students")
router.register('teachers', views.TeacherViewset, basename="teachers")
router.register('courses',views.CourseViewset, basename="courses")
router.register('rooms',views.RoomViewset, basename="rooms")
# router.register('classrooms',views.ClassRoomViewset, basename="classrooms")
router.register('registrations',views.RegistrationViewset, basename="registratios")
router.register('notes',views.NoteViewset, basename="notes")

urlpatterns = [
    path('', include(router.urls)),
    path('classrooms/course/<int:pk>/', views.OnlyListClassRoomViewset.as_view()),
]
