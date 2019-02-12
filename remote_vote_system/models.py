from django.db import models
from datetime import date
# Create your models here.
from enum import Enum

class Constituency(models.Model):
	name = models.CharField(max_length=200)

class User(models.Model):
	name = models.CharField(max_length=200)
	dob = models.DateField()
	state = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	constituency = models.CharField(max_length=200)
	STUDENT_TYPE_CHOICES = (
		('0', 'candidate'),
		('1', 'voter')
	)
	student_type = models.CharField(max_length=1, choices=STUDENT_TYPE_CHOICES)
	constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)	



class Vote(models.Model):
	user = models.ForeignKey(User,  on_delete=models.CASCADE)
	candidate_user_id = models.IntegerField(default=0)