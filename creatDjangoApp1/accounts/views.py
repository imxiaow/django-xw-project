from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	# this is a view 
	#return HttpResponse("home")
	return render(request, "accounts/dashboard.html") 

def products(request):
	# this is a view 
	#return HttpResponse("products")
	return render(request, "accounts/products.html")

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