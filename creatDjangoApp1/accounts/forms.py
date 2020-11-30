from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
	class Meta:
		# min two fields
		model = Order
		fields = '__all__' # form with all fields in it. 
		
