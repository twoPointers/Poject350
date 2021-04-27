from django.contrib import admin
from .models import Student , Result , Contact

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ('reg' , 'session' , 'name' , 'credits' , 'cgpa' )

@admin.register(Result)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('stuId', 'courseId' ,'courseName','semester','credit','isMajor','isLab','gpa')

@admin.register(Contact)
class StudentAdmin(admin.ModelAdmin):
    list_display= ('email' , 'desc')