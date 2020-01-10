from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Book, QUser


def index(request):
	num_books = Book.objects.all().count()
	num_users = QUser.objects.all().count()

	return render(
		request,
		'index.html',
		context={'num_books': num_books, 'num_users': num_users},
	)


class QUserCreationForm(UserCreationForm):
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
	)

	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
	)

	class Meta:
		model = QUser
		fields = ("username",)
		field_classes = {'username': UsernameField}

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		print(password2)

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def save(self, commit=True):
		print("save")
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


class RegisterFormView(FormView):
	form_class = QUserCreationForm

	success_url = "/catalog/login/"

	template_name = "login.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterFormView, self).form_valid(form)
