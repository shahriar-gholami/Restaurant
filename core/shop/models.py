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
	order_id = models.IntegerField()
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'{self.item.name} - {self.count}'

class OrderStatus(models.Model):
	status = models.CharField(max_length=250)

	def __str__(self):
		return self.status

class Order(models.Model):
	items = models.ManyToManyField(OrderItem)
	customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
	status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add = True)

	def get_total_price(self):
		total_price = 0
		for item in self.items.all():
			total_price = total_price + item.price * item.count
		return total_price

	@property
	def shamsi_created_date(self):
		return JalaliDatetime(self.created_date).strftime('%Y/%m/%d')