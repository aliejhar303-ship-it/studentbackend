from django.contrib import admin

# Register your models here.
# from .models import Student
# admin.site.register(Student) 

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name','fathername', 'email', 'age', 'phone', 'course', 'address')
    search_fields = ('name', 'email', 'course','phone')
    list_filter = ('course','age')
    ordering = ('name',) 