from django.contrib import admin
from django.contrib.auth import get_user_model 
from .forms import  UserAdminCreationForm , UserAdminChangeForm
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

User = get_user_model()



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('pk','email','name','lastname', 'is_admin', 'last_login')
    list_filter = ('is_admin','is_staff' , 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','name','lastname',)}),
        ('Permissions', {'fields': ('is_admin','is_staff' , 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('pk',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)




# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Content)
admin.site.register(Video)