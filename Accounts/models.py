from django.db import models
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

from django.db.models.signals import post_save , pre_save

import os
# Create your tests here.

class UserManager(BaseUserManager ):
	def create_user(self , email , password = None , is_staff = False , is_admin=False , is_active = True):
		if not email:
			raise ValueError('user must have an email adresse')
		user_obj = self.model(
			email = self.normalize_email(email),
					)
		user_obj.set_password(password)
		user_obj.is_staff = is_staff
		user_obj.is_admin = is_admin
		user_obj.is_active = is_active
		user_obj.save(using = self._db)
		return user_obj

	def create_staffuser(self , email  , password=None):
		user = self.create_user(
			email ,
			
			password,
			is_staff=True,
			is_active = True
			)
		return user

	def create_superuser(self , email , password=None):
		user = self.create_user(
			email ,
			password,
			is_staff=True,
			is_admin =True,
			is_active = True
			)
		return user






class User(AbstractBaseUser ,PermissionsMixin):
	email = models.EmailField(
		verbose_name='اسم المستخدم',
		max_length=255,
		unique=True,

	)
	name = models.CharField(max_length=100 , null=False , blank = False)
	lastname = models.CharField(max_length=100 , null=False , blank = False)
	is_active = models.BooleanField(default=True)
	is_staff    = models.BooleanField(default=False) # a admin user; non super-user
	is_admin = models.BooleanField(default=False) # a superuser
	# notice the absence of a "Password field", that's built in.
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # Email & Password are required by default.


	def get_full_name(self):
	# The user is identified by their email address
		return self.email


	def get_short_name(self):
	# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin
		
	def has_perms(self, perm, obj=None):
		return self.is_admin    
			
	def has_module_perms(self, app_label):
	   return self.is_admin

	@property
	def is_superuser(self):
		"Is the user superuser?"
		return self.superuser





	objects = UserManager()



