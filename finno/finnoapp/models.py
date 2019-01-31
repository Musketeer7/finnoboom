from django.db import models
from django.template.defaultfilters import slugify




class App(models.Model):
	user = models.CharField(max_length=30)
	appName = models.CharField(max_length=30)
	# IpAddress = models.GenericIPAddressField()
	IpAddress = models.CharField(max_length=30)
	appCode = models.CharField(max_length=30)
	companyName = models.CharField(max_length=255)
	webAddress = models.CharField(max_length=255)
	callBackUrl = models.CharField(max_length=255)
	activityType = models.CharField(max_length=255)
	# secredService
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'app'
		verbose_name_plural = 'apps'
		# ordering = ('created',)

	# def __str__(self):
	# 	return '%s %s' % (self.appName)
