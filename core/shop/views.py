from django.shortcuts import render
from django.views import View
import random
from random import randint
from .models import *
from .forms import ItemForm
from django.forms import formset_factory
from django.shortcuts import render
from django.views import View



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
	ItemsFormSet = formset_factory(ItemForm, extra=items_count)

	def get(self, request, *args, **kwargs):
		items = Item.objects.all()
		formset = self.ItemsFormSet()
		return render(request, 'shop/menu.html', {'formset': formset,'items':items})

	def post(self, request, *args, **kwargs):
		formset = self.ItemsFormSet(request.POST)
		if formset.is_valid():
			print('yesssssssssssssssssssss')


