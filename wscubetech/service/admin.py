from django.contrib import admin

# Register your models here.
from service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_title', 'service_description')


admin.site.register(Service)
