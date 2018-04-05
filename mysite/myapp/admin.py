from django.contrib import admin
from myapp import models
# Register your models here.
admin.site.register(models.Donor)
admin.site.register(models.Acceptor)
admin.site.register(models.Help)
