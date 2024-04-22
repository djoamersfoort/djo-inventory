from django.contrib import admin

from inventory import models

admin.site.register(models.Location)
admin.site.register(models.Item)
