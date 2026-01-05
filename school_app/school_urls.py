
from django.contrib import admin
from django.urls import path
from . import views
from .my_views import student_views, teacher_views, subject_views

urlpatterns = [
    path("", views.home, name="home"),
    path("find_by_id/<id>", views.find_by_id, name="find_by_id"),

    path("content", views.content, name="content"),

    path("students/index",student_views.index),

    path("students/show",student_views.show),

    path("students/create",student_views.create),

    path("students/delete/<id>", student_views.delete),

    path("students/edit/<id>", student_views.edit),

    path("students/update/<id>", student_views.update),

#Subject
    path("subjects/index",subject_views.index),

    path("subjects/show",subject_views.show),

    path("subjects/create",subject_views.create),

    path("subjects/delete/<id>", subject_views.delete),

    path("subjects/edit/<id>", subject_views.edit),

    path("subjects/update/<id>", subject_views.update),

#Teacher
    path("teachers/index",teacher_views.index),

    path("teachers/show",teacher_views.show),

    path("teachers/create",teacher_views.create),

    path("teachers/delete/<id>", teacher_views.delete),

    path("teachers/edit/<id>", teacher_views.edit),

    path("teachers/update/<id>", teacher_views.update)
]
