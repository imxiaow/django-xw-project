from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import EmailField

from .models import Order

class OrderForm(ModelForm):
	class Meta:
		# min two fields
		model = Order
		fields = '__all__' # form with all fields in it. 
		


class CreateUserForm(UserCreationForm):
	#email = forms.EmailField(required=True, label='Email')
	#email = EmailField(label=("Email address"), required=True, help_text=_("Required."))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		#fields = '__all__'