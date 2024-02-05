from django.contrib import admin
from .models import Student, Course


# Register your models here.
class ListStudents(admin.ModelAdmin):
    list_display = ['id', 'name', 'bi','created_at']
    list_display_links = ['id', 'name', 'bi']
    search_fields = ['name','bi']
    list_filter = ['id', "name"]
    list_per_page = 20

class ListCourses(admin.ModelAdmin):
    list_display = ['id', 'code', 'description','level','created_at']
    list_display_links =  ['id', 'code', 'description','level']
    search_fields = ['code','description']
    list_filter = ['id', 'code','description']
    list_per_page = 20


admin.site.register(Student, ListStudents)
admin.site.register(Course, ListCourses)