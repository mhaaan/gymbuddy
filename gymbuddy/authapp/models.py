from django.db import models

# Create your models here.
# This file we create database tables.
class WorkoutEntry(models.Model):
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

