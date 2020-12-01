from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import * 
from .forms import *
from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		#form = UserCreationForm()
		form = CreateUserForm()

		if request.method == 'POST':
			#form = UserCreationForm(request.POST)
			form = CreateUserForm(request.POST)

			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')

		context = {'form':form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method =="POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
				#return render(request, 'accounts/login.html', context)

		context = {}
		return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
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


@login_required(login_url='login')
def products(request):
	# this is a view 
	products = Product.objects.all()
	#return HttpResponse("products")
	return render(request, "accounts/products.html", {'products':products})


@login_required(login_url='login')
def customer(request, pk_test):
	# this is a view 
	# customer profile page
	#return HttpResponse("customer")
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer':customer, 'orders':orders, 'order_count': order_count, 'myFilter':myFilter}

	return render(request, "accounts/customer.html", context)


@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)

	customer = Customer.objects.get(id=pk)

	#form = OrderForm(initial={'customer':customer})
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)

	context = {'formset': formset}
	if request.method == "POST":
		#print("Printing POST: " + str(request.POST))
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save() # form is into the database
			return redirect('/')

	return render(request, "accounts/order_form.html", context)


@login_required(login_url='login')
def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	context = {'form': form}

	if request.method == "POST":
		#print("Printing POST: " + str(request.POST))
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save() # form is into the database
			return redirect('/')

	return render(request, "accounts/order_form.html", context)


@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	context = {'item':order}

	if request.method == "POST":
		order.delete()
		return redirect('/')

	return render(request, "accounts/delete.html", context)




"""
file structure the Django is looking for:

-- accounts
----templates
------accounts
--------dashboard.html
--------profile.html
--------customer.html

"""