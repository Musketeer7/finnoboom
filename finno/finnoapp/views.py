from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from finno.finnoapp.serializers import UserSerializer, AppSerializer

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
