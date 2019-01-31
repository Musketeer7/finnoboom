from django.db import models
from django.template.defaultfilters import slugify
from jsonfield import JSONCharField
from django.contrib.postgres.fields import JSONField, ArrayField


class App(models.Model):
	user = models.CharField(max_length=30)
	appName = models.CharField(max_length=30)
	IpAddress = models.GenericIPAddressField(protocol='both')
	# IpAddress = models.CharField(max_length=30)
	appCode = models.CharField(max_length=30)
	companyName = models.CharField(max_length=255)
	webAddress = models.CharField(max_length=255)
	callBackUrl = models.CharField(max_length=255)
	activityType = models.CharField(max_length=255)
	# selectedservice =  JSONField()
	# selectedservice = models.ManyToManyField(SelectedService)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (str(self.appName))

	class Meta:
		verbose_name = 'app'
		verbose_name_plural = 'apps'
		# ordering = ('created',)

class Service(models.Model):
	class Meta:
		verbose_name = 'service'
		verbose_name_plural = 'services'

	app = models.ForeignKey(App, related_name='services', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	# {'name': 'gdgs', 'value': 'gdfgdfg'}

	def __unicode__(self):
		return '%d: %s' % (self.name, self.value)
