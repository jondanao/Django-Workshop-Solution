from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.title


class Article(models.Model):
	DRAFT = 1
	PUBLISHED = 2
	STATUS_CHOICES = [
		(DRAFT, 'Draft'),
		(PUBLISHED, 'Published')
	]

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	body = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
	pub_date = models.DateTimeField(default=datetime.now)
	category = models.ForeignKey(Category)
	author = models.ForeignKey(User)
	image = models.ImageField(upload_to='photos')

	def __unicode__(self):
		return self.title

