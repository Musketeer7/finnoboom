from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from finno.finnoapp.serializers import UserSerializer, AppSerializer, ServiceSerializer

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from . import models
from . import serializers



class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class AppViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Apps to be viewed or edited.
	"""
	queryset = models.App.objects.all()
	serializer_class = AppSerializer


class ServiceViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Apps to be viewed or edited.
	"""
	queryset = models.Service.objects.all()
	serializer_class = ServiceSerializer



def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('http://127.0.0.1:8000/')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


#========================
"""
class SomeView(ListCreateAPIView):
	queryset = SomeModel.objects.all()
	serializer_class = SomeModelSerializer
	filter_backends = (OrderingFilter, DjangoFilterBackend)
	filter_class = CustomFilter
	ordering = ('id',)

	def list(self, request, *args, **kwargs):
		if request.GET.get('all', None):
			# Do something
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return super(SomeView, self).list(self, request, *args, **kwargs)


class SomeView(ListCreateAPIView):
	queryset = SomeModel.objects.all()
	serializer_class = SomeSerializer
	filter_backends = (OrderingFilter, DjangoFilterBackend)
	filter_class = CustomFilter
	ordering = ('id',)

	def list(self, request, *args, **kwargs):
		if request.GET.get('all', None):
			queryset = self.filter_queryset(self.get_queryset())
			self.pagination_class.default_limit = queryset.count()  # The problem is this line

			page = self.paginate_queryset(queryset)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

			serializer = self.get_serializer(queryset, many=True)

			return Response(serializer.data)
		else:
			return super(SomeView, self).list(self, request, *args, **kwargs)

"""