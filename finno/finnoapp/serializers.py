from django.contrib.auth.models import User
from rest_framework import serializers
from .models import App, Service
from jsonfield import JSONCharField
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.validators import validate_ipv4_address


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class ServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		fields = ('name', 'value', 'app')



class AppSerializer(serializers.Serializer):
	"""Transaction Serializer."""

	class Meta:
		model = App
		fields = ('user', 'appName', 'IpAddress', 'appCode', 'companyName', 'webAddress', 'callBackUrl', 'activityType', 'selectedService', 'created_on')

	id = serializers.IntegerField(read_only=True)
	appName = serializers.CharField(required=True, allow_blank=False, max_length=30)
	IpAddress = serializers.CharField(validators=[validate_ipv4_address])
	appCode = serializers.CharField(max_length=30)
	companyName = serializers.CharField(max_length=255)
	webAddress = serializers.CharField(max_length=255)
	callBackUrl = serializers.CharField(max_length=255)
	activityType = serializers.CharField(max_length=255)
	# selectedervice = JSONField()
	created_on = serializers.DateTimeField()

	services = ServiceSerializer(many=True,required=False)

	def create(self, validated_data):
		services_data = validated_data.pop('services')
		service = Service.objects.create(**validated_data)
		for service_data in services_data:
			Service.objects.create(app=app, **track_data)
		return app



	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return App.objects.create(**validated_data)

