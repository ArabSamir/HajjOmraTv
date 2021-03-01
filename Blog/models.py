from django.db import models
from Accounts.models import User
from django.db.models.signals import post_save , pre_save
from random import choice
from string import ascii_letters
from ckeditor.fields import RichTextField
# seed random number generator

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Category(models.Model):
	category_name = models.CharField(max_length=250 , blank=False , null=False)

	def __str__(self):
		return category_name



class Post(models.Model):
	title = models.CharField(max_length=250 , blank=False, null=False)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User , on_delete=models.CASCADE , blank=False , null=False)
	content =  RichTextField()
	statut = models.IntegerField(choices=STATUS, default=0)
	updated_on = models.DateTimeField(auto_now= True)
	category = models.ForeignKey(Category , on_delete=models.CASCADE , blank=False , null=False)
	created_on = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title



def create_post_slug(instance , new_slug = None):
	'''
		This function generates a slug for the profile using the user name, lasname
	'''
	title = instance.title

	value = choice(ascii_letters)
	slug  = slugify(f'{title}{ascii_letters}')
	
	if new_slug is not None:
		slug = new_slug
	qs  = Post.objects.filter(slug = slug).order_by('-id')
	exists = qs.exists()
	if exists:
		
		value = choice(ascii_letters)
		# generate a new slug using a random  int value
		new_slug = f'{slug}{value}'
		 
		return create_post_slug(instance , new_slug=new_slug)

	return slug

def pre_save_post_slug_creator(sender , instance , **kwargs):
	'''
		This function saves the generated slug to the profile instance
	'''
	if not instance.slug:
		instance.slug = create_profile_slug(instance)

pre_save.connect(pre_save_post_slug_creator , sender=Post)
