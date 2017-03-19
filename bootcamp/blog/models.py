from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=20)
	# object represent function 
	def __str__(self):
		return self.name  



class BlogPost(models.Model):
	author=models.ForeignKey(User)
	category=models.ForeignKey(Category)
	title=models.CharField(max_length=200)
	content=models.TextField()

	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True) # automatically take the date from device 
	publish_date=models.DateTimeField()
	publish=models.BooleanField(default=False)

	

	file=models.FileField(null=True,blank=True,upload_to='Blog_post/Files/%Y/%m')
	image=models.ImageField(upload_to='Blog_post/Images/%Y-%m-%d')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created',)