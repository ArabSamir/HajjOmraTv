from django.db import models
from Accounts.models import User
from django.db.models.signals import post_save , pre_save
from random import choice
from string import ascii_letters
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
# seed random number generator

# Create your models here.

STATUS = (
	(0,"مسودة"),
	(1,"ينشر")
)


class Category(models.Model):
	category_name = models.CharField(verbose_name=_('إسم الفئة'),max_length=250 , blank=False , null=False)
	class Meta:
		verbose_name = _('ﺔﺌﻔﻟا')
		verbose_name_plural = _('الفئات')
	def __str__(self):
		return self.category_name



class Post(models.Model):
	title = models.CharField(verbose_name=_('العنواة'),max_length=250 , blank=False, null=False)
	image = models.ImageField(verbose_name=_('الصورة'),upload_to='blog/posts' ,  blank=True, null=True)
	author = models.ForeignKey(User , on_delete=models.CASCADE , blank=False , null=False,verbose_name=_('الكاتب'))
	description =  models.TextField(verbose_name=_('الشرح'),)
	content =  RichTextFieldverbose_name=_('المحتوى'),()
	statut = models.IntegerField(verbose_name=_('الحالة'),choices=STATUS, default=0)
	updated_on = models.DateTimeField(auto_now= True)
	category = models.ForeignKey(Category , on_delete=models.CASCADE , blank=False , null=False,verbose_name=_('الفئة'))
	created_on = models.DateTimeField(verbose_name=_('Category ID'),auto_now_add=True)
	
	class Meta:
		ordering = ['-created_on']

	
	class Meta:
		verbose_name = _('مقال')
		verbose_name_plural = _('مقالات')

	def __str__(self):
		return self.title


