from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
# Create your views here.
@csrf_exempt
def add_sell_buy(request):
	response_json={}
	if request.method=='POST':
		
		try:
			category_id=request.POST.get('category_id')
			access_token=request.POST.get('access_token')
			json=jwt.decode(str(access_token),'999123',algorithms=['HS256'])
			mobile = json["mobile"]
			product_name=request.POST.get('product_name')
			product_description=request.POST.get('product_description')
			product_price=request.POST.get('product_price')
			product_unit=request.POST.get('product_unit')
			sell_buy_data.objects.create(category_id=category_id,mobile=mobile,product_name=product_name,product_price=product_price,product_description=product_description,product_unit=product_unit)
			response_json['success']=True
			response_json['message']='Requirement Successfully Submitted'
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='Something Went Wrong'
	else:
		response_json['success']=False
		response_json['message']='I am a Big Hacker get out of here for your safety'
	return JsonResponse(response_json)

