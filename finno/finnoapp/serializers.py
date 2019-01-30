from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class AppSerializer(serializers.Serializer):
	class Meta:
		model = User
		fields = ('user', 'appName', 'IpAddress', 'appCode', 'companyName', 'webAddress', 'callBackUrl', 'activityType', 'created_on')


