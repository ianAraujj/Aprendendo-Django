from django.db import models

# Create your models here.

class CursosManager(models.Manager):

    def procurar(self, query):
        return self.get_queryset().filter(name__icontains=query)

class Cursos(models.Model):
    name = models.CharField('Nome', max_length=90)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    startDate = models.DateField('Data de Início', null=True, blank=True)

    created = models.DateTimeField('Data de criação', auto_now_add=True)
    modify = models.DateTimeField('Data de Modificação', auto_now=True)

    objects = CursosManager()

    def __str__(self):
        return self.name
