from django.contrib.auth 			import login as login_auth, logout , authenticate
from django.contrib.auth.forms		import AuthenticationForm , PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts 				import render , redirect,get_object_or_404 
from django.http                    import HttpResponse
from .models                        import User
from .forms                         import *
from django.contrib import messages
from django.utils.encoding          import force_text
import json 
from django.contrib 				import messages

from django.utils.encoding          import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http              import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader         import render_to_string
from django.core.mail               import EmailMessage
from datetime import date
from django.conf                    import settings


def signup(request):
	'''
		this function renders the service provider sign up page (registration)
	'''
	template_name = 'registration/signup.html'
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			try:
				
				form.save()
				messages.success(request, 'Bienvenu')
				return redirect('index')
			except Exception as e:
				messages.error(request, 'error')
				return redirect('index')

	args = {'form' : form}
	return render(request, template_name, args)




@login_required
def change_password(request):
	'''
		this function is to change the user password when user is logged in
	'''
	template_name = 'password_reset/change_password.html'
	if request.method == 'POST':
		form = ChangePasswordForm(data=request.POST , user = request.user)

		if form.is_valid():
			form.save()
			messages.success(request , 'Mot de passe Modifier')
			return redirect('change_password')
	   
		else:
		
			args =  {
					'form' : form ,
					}
			return render(request , template_name , args)

	else:
		form = ChangePasswordForm(user = request.user)

		args =  {'form' : form }

		return render(request , template_name , args)
	

