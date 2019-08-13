from django.db import models

# Create your models here.

class Cursos(models.Model):
    name = models.CharField('Nome', max_length=90)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    startDate = models.DateField('Data de Início', null=True, blank=True)

    created = models.DateTimeField('Data de criação', auto_now_add=True)
    modify = models.DateTimeField('Data de Modificação', auto_now=True)
