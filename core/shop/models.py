from django.db import models
from django.utils import timezone
from khayyam import JalaliDatetime

class Customer(models.Model):
	name = models.CharField(max_length=250)
	phone_number = models.CharField(max_length=11)
	address = models.CharField(max_length=1000)

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=250)
	price = models.PositiveIntegerField(default=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class OrderItem(models.Model):
	order_id = models.IntegerField(default=100000)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'{self.item.name} - {self.count}'

class Order(models.Model):
	order_id = models.IntegerField(default=100000)
	items = models.ManyToManyField(OrderItem)
	customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
	status = models.BooleanField(default=False)
	category = models.CharField(max_length=250, null=True, blank=True)
	payment_method = models.CharField(max_length=250, null=True, blank=True)
	delivery = models.BooleanField(default=False)
	delivery_price = models.IntegerField(default=0)
	payment_status = models.BooleanField(default=False)

	created_date = models.DateTimeField(auto_now_add = True)

	def get_total_price(self):
		total_price = 0
		for item in self.items.all():
			total_price = total_price + item.price * item.count
		total_price = total_price + self.delivery_price
		return total_price

	@property
	def shamsi_created_date(self):
		return JalaliDatetime(self.created_date).strftime('%Y/%m/%d')