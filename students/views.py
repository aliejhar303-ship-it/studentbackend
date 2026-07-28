from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


# ===========================
# Register
# ===========================
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password Match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Username Exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Create User
        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "students/register.html")


# ===========================
# Login
# ===========================
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("student_list")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "students/login.html")


# ===========================
# Logout
# ===========================
def logout_user(request):
    logout(request)
    return redirect("login")


# ===========================
# Student List + Search
# ===========================
@login_required
def student_list(request):
    q = request.GET.get("q")

    if q:
        students = Student.objects.filter(
            Q(name__icontains=q) |
            Q(fathername__icontains=q) |
            Q(course__icontains=q) |
            Q(phone__icontains=q)
        )
    else:
        students = Student.objects.all()

    total_students = Student.objects.count()

    return render(request, "students/student_list.html", {
        "students": students,
        "total_students": total_students,
    })


# ===========================
# Add Student
# ===========================
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {
        "form": form
    })


# ===========================
# Edit Student
# ===========================
@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {
        "form": form,
        "student": student
    })


# ===========================
# Delete Student
# ===========================
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    messages.success(request, "Student deleted successfully.")
    return redirect("student_list")