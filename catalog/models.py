from django.db import models
from django.urls import reverse


class Book(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])


class Users(models.Model):
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=200)
	email = models.EmailField()
	vk = models.CharField(max_length=200)
	insta = models.CharField(max_length=200)
	info = models.CharField(max_length=200)
	avatarka = models.ImageField()
	filename = models.ImageField()
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	reiting = models.IntegerField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('user-detail', args=[str(self.id)])