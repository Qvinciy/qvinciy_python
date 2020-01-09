from django.shortcuts import render

from .models import Book, Users


def index(request):
	num_books = Book.objects.all().count()
	num_users = Users.objects.all().count()

	return render(
		request,
		'index.html',
		context={'num_books': num_books, 'num_users': num_users},
	)


def login(request):
	return render(
		request,
		'login.html'
	)
