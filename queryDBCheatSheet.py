# 1) Return all customers from customer table
customers = Customer.objects.all()

#2) returns first customer in table
firstCustomer = Customer.objects.first()

#3) Return last customer in the table
lastCustomer = Customer.objects.last()

#4) Return single customer by name
customerByName = Customer.objects.get(name = "Wendy Qi")


#5) return single customer by ID
customerById = Customer.objects.get(id=2)

#6) return all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#7) Return orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name


#8) Returns products from products table with value of "Outdoor" in category attributes 
product = Product.objects.filter(category="Outdoor")


#9) order/sort objects by id
leastToGreatest = Product.objects.all().order_by("id")
greatestToLeast = Product.objects.all().order_by("-id")


# 10) Returns all products with tag of "Sports": (query many to many Field)
productsFiltered = Product.objects.filter(tags__name="Sports")


# if the customer has more than 1 ball, how would you reflect it in the database?

# Answer: Because there are many different products and this value changes constantly you
# 			would most likely not want to store the value in the database but rather just make this 
#			function we can run each time we load the customers profile. 


# Return the total count for number of time a "BAll" was ordered by the first cutomer.
ballOrders = firstCustomer.order_set.filter(product__name = "Ball").count()

# return total count for each product ordered
allOrders={}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] +=1
	else:
		allOrders[order.product.name] = 1

# returns: allOrders:{"Ball":2, "BBQ Grill": 1}



#### RElated SET EXAMPLE 
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name=models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#return all child models related to parent
parent.ChildModel_set.all()
