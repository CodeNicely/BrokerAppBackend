from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def get_categories(request):
	response_data={}
	if request.method=='GET':
		try:
			category_list=[]
			category_list_data=category_data.objects.filter(show=True)
			for o in category_list_data:
				category_details={}
				category_details['id']=o.id
				category_details['name']=o.name
				category_details['description']=o.description
				category_list.append(category_details)
			unit_list_data=unit_data.objects.filter()
			unit_list=[]
			for o in unit_list_data:
				unit_list.append(o.name)
			response_data['success']=True
			response_data['message']='Successful'
			response_data['category_list']=category_list
			response_data['unit_list']=unit_list
		except Exception,e:
			print e
			response_data['success']=False
			response_data['message']='Error Occured '+str(e)
	else:
		response_data['success']=False
		response_data['message']='You better get out of here'
	print JsonResponse(response_data)
	return JsonResponse(response_data)


@csrf_exempt
def get_products(request):
	response_data={}
	if request.method=='GET':
		try:
			category_id=request.GET.get('category_id')
			product_list=[]
			product_list_data=product_data.objects.filter(show=True,category_id=category_id)
			for o in product_list_data:
				product_details={}
				product_details['id']=o.id
				product_details['name']=o.name
				product_details['description']=o.description
				product_details['image']=request.scheme+'://'+request.get_host()+'/media/'+str(o.image)
				product_details['price']=o.price
				product_details['unit']=o.unit
				product_list.append(product_details)
			response_data['success']=True
			response_data['message']='Successful'
			response_data['product_list']=product_list
		except Exception,e:
			print e
			response_data['success']=False
			response_data['message']='Error Occured '+str(e)
	else:
		response_data['success']=False
		response_data['message']='You better get out of here'
	print JsonResponse(response_data)
	return JsonResponse(response_data)