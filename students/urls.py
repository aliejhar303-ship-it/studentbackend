from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),

    path("add/", views.add_student, name="add_student"),
    path("edit/<int:id>/", views.edit_student, name="edit_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),

]