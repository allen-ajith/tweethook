from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm,CustomUserChangeForm
from .models import Tweet,User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fiel
class Uadmin(UserAdmin):
	add_form = SignUpForm
	form = CustomUserChangeForm
	model = User
	list_display = ['username','twitter_handle']
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('twitter_handle')}),
		)
	fieldsets = UserAdmin.fieldsets

admin.site.register(Tweet)
admin.site.register(User,Uadmin)