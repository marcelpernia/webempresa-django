from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre')

	class Meta:
		verbose_name = 'categoria'
		verbose_name_plural = 'categorias'

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='Título')
	img = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name='Imagen')
	content = models.TextField(verbose_name='Contenido')
	published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
	categories = models.ManyToManyField(Category, verbose_name='Categoría', related_name='get_posts')
	author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'entrada'
		verbose_name_plural = 'entradas'

	def __str__(self):
		return self.title