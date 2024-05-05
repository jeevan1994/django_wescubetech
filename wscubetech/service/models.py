from django.db import models


# Create your models here.

class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=100)
    service_description = models.TextField()
    img = models.FileField(upload_to='icon',null=True)
