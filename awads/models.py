from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank = True ,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField( default='Blank-Avatar.JPG', null = True , blank = True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	TYPE = (
			('Urgent', 'Urgent'),
			('Not Urgent', 'Not Urgent'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	urgent = models.CharField(max_length=200,null=True,choices=TYPE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200,  choices=STATUS, default = 'Pending')
	note = models.CharField(max_length=1000, null=True)
	AssetName = models.CharField(max_length=100,null=True)
	quantity = models.IntegerField(null=True)
	reason = models.TextField(max_length=200,null=True)

	def __str__(self):
		return self.product.name
		
		
