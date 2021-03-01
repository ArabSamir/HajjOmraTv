from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (ReadOnlyPasswordHashField, 
                                        UserCreationForm,  
                                        UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm , PasswordChangeForm)
from .models import User
from django.contrib.auth import authenticate, login , password_validation




class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email', 'name': 'email', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control','autofocus': True ,'placeholder': 'Mot de passe', }))



class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Votre adresse e-mail :', }))
   


class PasswordSetForm(SetPasswordForm):
   
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Le nouveau mot de passe :' , }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez le nouveau mot de passe :'}),
    )


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Ancien mot de passe :"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Le nouveau mot de passe :"}),
    )

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Confirmez le nouveau mot de passe :"}),
    )

#--------------user creation form-----------------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    password1 = forms.CharField(
        label = 'Mot de passe',
        strip=False,
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label = 'Confirmation',
        strip=False,
        widget=forms.PasswordInput,

    )



    email.widget.attrs.update({'class': 'form-control','autofocus': True ,'placeholder':'E-mail'})
    name.widget.attrs.update({'class': 'form-control','autofocus': True ,'placeholder':'Prénom'})
    lastname.widget.attrs.update({'class': 'form-control','autofocus': True ,'placeholder':'Nom'})
    password1.widget.attrs.update({'class': 'form-control','autofocus': True, 'placeholder':'Mot de passe'})
    password2.widget.attrs.update({'class': 'form-control','autofocus': True , 'placeholder':'Confirmé le Mot de passe' })
    
    class Meta:
        model = User
        fields = (
            'email', 
            'password1',
            'password2',
            'name',
            'lastname',
            )

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)
        if users.exists():
            if not users[0].is_active:
                try:
                    send_email_confirmation('',users[0] ,self )
                    
                except Exception as e:
                    raise forms.ValidationError("E-mail n\'a pas été envoyé")
                raise forms.ValidationError("User  existe déjà verifier votre boite email pour activer ce compte.")
        return email


    

#--------------end user creation form-----------------



class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]