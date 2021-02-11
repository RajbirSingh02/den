from django.db import models


class Appointment(models.Model):
	name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.EmailField(max_length=100)
	address = models.CharField(max_length=100)
	schedule = models.TimeField()
	date = models.DateField()
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.name


	