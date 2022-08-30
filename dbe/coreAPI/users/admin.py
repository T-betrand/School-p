from django.contrib import admin
from .models import User, ServiceProvider, Skills, Jobs

# Register your models here.
admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Skills)
admin.site.register(Jobs)