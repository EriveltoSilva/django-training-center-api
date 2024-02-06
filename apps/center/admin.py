from django.contrib import admin
from .models import *

class ListStudents(admin.ModelAdmin):
    list_display = ['user','bi', 'gender','race','civil_status','birthday','created_at',]
    list_display_links = ['user','bi', 'birthday', 'created_at',]
    search_fields = ['user','bi','birthday',]
    list_filter = ['id', 'birthday','gender','race','civil_status',]
    list_per_page = 20
admin.site.register(Student, ListStudents)

class ListTeachers(admin.ModelAdmin):
    list_display = ['user','bi', 'formation_area','gender','race','civil_status','created_at',]
    list_display_links = ['user','bi','formation_area','created_at',]
    search_fields = ['user','bi', 'formation_area']
    list_filter = ['id', 'gender','race','civil_status',]
    list_per_page = 20

admin.site.register(Teacher, ListTeachers)


class ListCourses(admin.ModelAdmin):
    list_display = ['id', 'code', 'description','duraction','duraction_unit','created_at']
    list_display_links =  ['id', 'code', 'description','duraction', 'duraction_unit']
    search_fields = ['code','description','duraction']
    list_filter = ['id', 'code','description', 'duraction']
    list_per_page = 20

admin.site.register(Course,ListCourses)

class ListRooms(admin.ModelAdmin):
    list_display = ['id', 'name', 'number',]
    list_display_links =  ['id', 'name', 'number',]
    search_fields = ['name','number',]
    list_filter = ['id', 'name','number',]
    list_per_page = 20

admin.site.register(Room, ListRooms)


class ListClassRoom(admin.ModelAdmin):
    list_display = ['id', 'course', 'teacher','room','status']
    list_display_links =  ['id', 'course', 'teacher','room', 'status']
    search_fields = ['course','teacher','room', 'status']
    list_filter = ['id', 'course','teacher', 'room', 'status',]
    list_per_page = 20

admin.site.register(ClassRoom,ListClassRoom)

class ListRegistration(admin.ModelAdmin):
    list_display = ['id', 'class_room','student','data']
    list_display_links =  ['id', 'class_room','student','data']
    search_fields = ['class_room','student','data']
    list_filter = ['id', 'class_room','student','data',]
    list_per_page = 20

admin.site.register(Registration,ListRegistration)

class ListNote(admin.ModelAdmin):
    list_display = ['id', 'teacher','student','value','class_room',]
    list_display_links =  ['id', 'teacher','student','value','class_room',]
    search_fields = ['teacher','student','value','class_room',]
    list_filter = ['id', 'teacher','student','value','class_room',]
    list_per_page = 20

admin.site.register(Note,ListNote)

