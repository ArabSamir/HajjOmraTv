from django.shortcuts import render , get_object_or_404
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def post_detail(request , pk):
	template_name = 'post_detail.html'
	posts = Post.objects.all().order_by('-created_on')
	last_posts = posts[:3]

	post = get_object_or_404(Post , pk=pk) 
	args ={
		'post':post,
		'last_posts':last_posts,
	}

	return render(request , template_name , args)

def blog(request):
	template_name = 'blog.html'

	posts = Post.objects.all().order_by('-created_on')
	last_posts = posts[:3]
	paginator = Paginator(posts, 3) # Show 25 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	args = {
		'last_posts':last_posts,
		'posts':page_obj,
		'page_obj':page_obj,
	}

	return render(request , template_name , args)