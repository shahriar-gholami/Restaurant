from django.shortcuts import render, redirect
from django.views import View
import random
from random import randint
from .models import *
from .forms import *
from django.forms import formset_factory




class IndexView(View):

	def get(self, request):

		return render(request, 'shop/index.html')

# class OrderItemsView(View):

# 	template_name = 'shop/menu.html'

# 	def get(self, request):
# 		order_id = random.randint(100000,999999)
# 		form = NewOrderItemsForm
# 		items = Item.objects.all()
# 		return render(request, self.template_name, {'form':form, 'items':items, 'order_id':order_id})

# 	def post(self, request, *args, **kwargs):
# 		form = NewOrderItemsForm(request.POST)
# 		if form.is_valid():
# 			items = Item.objects.all()
# 			order_id = form.cleaned_data['order_id']
# 			item = form.cleaned_data['item']
# 			count = form.cleaned_data['count']
# 			selected_item = Item.objects.get(name = item)
# 			new_order_item = OrderItem.objects.create(
# 				item = selected_item,
# 				count = count,
# 				order_id = order_id
# 			)
# 			return render(request, self.template_name, {'form':form, 'items':items, 'order_id':order_id, 'message':'the order is submitted'})


class NewOrderItemsView(View):
	items_count = Item.objects.all().count()

	def get(self, request, *args, **kwargs):

		form = DynamicItemForm
		items = Item.objects.all()
		return render(request, 'shop/menu.html', {'form': form,'items':items})

	def post(self, request, *args, **kwargs):
		form = DynamicItemForm(request.POST)
		order_id = random.randint(100000,999999)
		if form.is_valid():
			# print(form.cleaned_data)
			for key,value in form.cleaned_data.items():
				item = Item.objects.get(name=key)
				new_order_item = OrderItem.objects.create(
					order_id = order_id,
					item = item,
					count = value
				)
			new_order = Order.objects.create(
				order_id = order_id,
			)
			for item in OrderItem.objects.all():
				if item.order_id == order_id and item.count != 0:
					new_order.items.add(item)
			return redirect('shop:add_customer', order_id)

class NewOrderCustomerView(View):

	template_name = 'shop/add-customer.html'

	def get(self, request, order_id):
		order = Order.objects.get(order_id = order_id)
		customers = Customer.objects.all()
		form = NewCustomerForm
		return render(request, self.template_name, {'order':order, 'customers':customers, 'form':form})

	def post(self, request, order_id):
		form = NewCustomerForm(request.POST)

		if form.is_valid():
			new_customer = Customer.objects.create(
				name = form.cleaned_data['name'],
				phone_number = form.cleaned_data['phone_number'],
				address = form.cleaned_data['address']
			)
			order = Order.objects.get(order_id = order_id)
			return redirect('shop:select_customer', order_id, new_customer.id)

class SelectOrderCustomerView(View):

	def get(self, request, order_id, customer_id):
		order = Order.objects.get(order_id=order_id)
		customer = Customer.objects.get(id=customer_id)
		order.customer = customer
		order.save()
		return redirect('shop:order_payment', order_id)
	
class PaymentDetailView(View):

	template_name = 'shop/payment-detail.html'

	def get(self, request, order_id):
		form = OrderDetailForm
		return render(request, self.template_name, {'form':form})

	def post(self, request, order_id):
		order = Order.objects.get(order_id = order_id)
		form = OrderDetailForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			order.category = form.cleaned_data['category']
			order.payment_method = form.cleaned_data['payment']
			order.save()
			return redirect('shop:index')















