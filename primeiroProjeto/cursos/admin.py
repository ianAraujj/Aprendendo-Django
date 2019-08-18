from django.contrib import admin

# Register your models here.

# importei e registrei o meu model
from .models import Cursos
admin.site.register(Cursos)