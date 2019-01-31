from django.contrib.auth.models import User
from rest_framework import serializers
from .models import App


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class AppSerializer(serializers.Serializer):
	
	id = serializers.IntegerField(read_only=True)
	appName = serializers.CharField(required=True, allow_blank=False, max_length=30)
	IpAddress = serializers.CharField(max_length=30)
	appCode = serializers.CharField(max_length=30)
	companyName = serializers.CharField(max_length=255)
	webAddress = serializers.CharField(max_length=255)
	callBackUrl = serializers.CharField(max_length=255)
	activityType = serializers.CharField(max_length=255)

	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return App.objects.create(**validated_data)

	# class Meta:
		# model = User
		# fields = ('user', 'appName', 'IpAddress', 'appCode', 'companyName', 'webAddress', 'callBackUrl', 'activityType', 'created_on')


