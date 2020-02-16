from django import forms
from django.contrib.auth.views import LogoutView
from django.forms.widgets import Input
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

from django.contrib.auth import (
	authenticate, login, logout
)

from django.utils.html import format_html, format_html_join

from .models import Book, QUser, UserProfile

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class QErrorList(ErrorList):
	def as_ul(self):
		if not self.data:
			return ''

		return format_html(
			'<ul class="{}">{}</ul>',
			self.error_class,
			format_html_join('', '<li>{}</li>', ((e,) for e in self))
		)


class QTextInput(Input):
	input_type = 'text'
	template_name = 'text.html'


class QPasswordInput1(forms.PasswordInput):
	template_name = 'password1.html'


class QPasswordInput2(forms.PasswordInput):
	template_name = 'password2.html'


class QUsernameField(UsernameField):
	pass


class QCharField(forms.CharField):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class QUserCreationForm(UserCreationForm):
	num_users = QUser.objects.all().count()
	users_list = QUser.objects.order_by('-rating').all()

	password1 = QCharField(
		widget=QPasswordInput1(attrs={'autocomplete': 'new-password'})
	)

	password2 = QCharField(
		widget=QPasswordInput2(attrs={'autocomplete': 'new-password'}),
	)

	def __init__(self, *args, **kwargs):
		super().__init__(error_class=QErrorList, *args, **kwargs)
		if self._meta.model.USERNAME_FIELD in self.fields:
			self.fields[self._meta.model.USERNAME_FIELD].widget = QTextInput(attrs={'autofocus': True})

	class Meta:
		model = QUser
		fields = ("username",)
		field_classes = {'username': QUsernameField}

	def as_p(self):
		return self._html_output(
			normal_row='%(field)s',
			error_row='%s',
			row_ender='',
			help_text_html='',
			errors_on_separate_row=True,
		)


class RegisterFormView(FormView):

	def setup(self, request, *args, **kwargs):
		self.request = request
		self.args = args
		self.kwargs = kwargs

		password2 = request.POST.get('password2', '0')
		if password2 == '1':
			username = request.POST.get('username', '')
			password1 = request.POST.get('password1', '')
			if username != '' and password1 != '':
				try:
					self.request.user = authenticate(request=self.request, username=username, password=password1)
					login(request, self.request.user)
				except Exception as ex:
					print(ex)

	form_class = QUserCreationForm

	success_url = "/"

	template_name = "login_authenticated.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterFormView, self).form_valid(form)


class QLogoutView(LogoutView):
	success_url = "/"
	next_page = "/"


def index(request):
	num_users = QUser.objects.all().count()

	return render(
		request,
		'index.html',
		context={'num_users': num_users},
	)


class QUserView(APIView):
	def get(self, request):
		users = QUser.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response({"users": serializer.data})
