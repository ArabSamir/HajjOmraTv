from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib 				import messages
from .forms import *
from Accounts.models import Contact , Content

# Create your views here.

def post_detail(request , pk):
	template_name = 'post_detail.html'
	post = get_object_or_404(Post , pk=pk) 
	posts = Post.objects.all().order_by('-created_on')
	last_posts = posts[:3]
	comments = Comment.objects.filter(post=post)
	nb_comments = comments.count()
	print(f'nb comments {nb_comments}')
	form = CommentForm(request.POST or None)
	contact = Contact.objects.all()[0]
	content = Content.objects.all()[0]
	
	if request.method == "POST":
		if form.is_valid():
			try:
				comment =form.save(commit=False)
				comment.creator = request.user
				comment.post = post
				comment.save()
				messages.success(request, 'تم إنشاء التعليق بنجاح')
			except Exception as e:
				messages.error(request, f'لم يتم إنشاء التعليق {e}')
							
			return redirect('post_detail' , pk=pk)

	args ={
		'nb_comments':nb_comments,
		'comments':comments,
		'post':post,
		'form':form,
		'last_posts':last_posts,
		'contact':contact,
	    'content':content,
	}

	return render(request , template_name , args)

def blog(request):
	template_name = 'blog.html'

	posts = Post.objects.all().order_by('-created_on')
	last_posts = posts[:3]
	paginator = Paginator(posts, 3) # Show 25 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	contact = Contact.objects.all()[0]
	content = Content.objects.all()[0]

	args = {
		'last_posts':last_posts,
		'posts':page_obj,
		'page_obj':page_obj,
		
		'contact':contact,
	    'content':content,
	}

	return render(request , template_name , args)