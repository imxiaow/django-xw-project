from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import * 

def home(request):
	# this is a view 
	#return HttpResponse("home")
	orders= Order.objects.all()
	customers=Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status="Delivered").count()
	pending = orders.filter(status="Pending").count()


	context = {'orders':orders, 'customers':customers, 
	'total_orders': total_orders, 'delivered':delivered, 
	'pending':pending}

	return render(request, "accounts/dashboard.html", context) 

def products(request):
	# this is a view 
	products = Product.objects.all()
	#return HttpResponse("products")
	return render(request, "accounts/products.html", {'products':products})

def customer(request):
	# this is a view 
	# customer profile page
	#return HttpResponse("customer")
	return render(request, "accounts/customer.html")


"""
file structure the Django is looking for:

-- accounts
----templates
------accounts
--------dashboard.html
--------profile.html
--------customer.html

"""