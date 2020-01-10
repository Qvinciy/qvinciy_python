from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class QUser(AbstractUser):
	avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')
	filename = models.ImageField(upload_to='images/users', verbose_name='Изображение')

	login = models.CharField(max_length=20)

	vk = models.CharField(max_length=200)
	instagram = models.CharField(max_length=200)

	info = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		swappable = 'AUTH_USER_MODEL'


class UserProfile(models.Model):
	user = models.OneToOneField(QUser, on_delete=models.CASCADE, primary_key=True)

	def __unicode__(self):
		return self.user

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'


class Book(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

