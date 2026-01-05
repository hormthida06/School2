from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="Date of Birth")
    address = models.TextField()

# --------------------------
# SUBJECT MODEL
# --------------------------
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)

# --------------------------
# TEACHER MODEL
# --------------------------
class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="Date of Birth")
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
