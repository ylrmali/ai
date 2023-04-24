from django.contrib import admin
from project.models import User, Project, ColorSpace

# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(ColorSpace)
