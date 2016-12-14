from django.shortcuts import render
from .models import *
import jwt
from django.http import JsonResponse
from login.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def final_deals_to_show(request):
	try:
		access_token=request.POST.get("access_token")

		try:
			json=jwt.decode(str(access_token),"999123",algorithm=["HS256"])
			print json["mobile"]
			if login_user.objects.filter(mobile=int(json["mobile"])).exists():
				response_json={}
				response_json["success"]=True
				response_json["message"]="all deals"
				response_json["deals"]=[]
				for row in deals.objects.all():
					temp_json={}
					temp_json["product_name"]=row.product_name
					temp_json["quantity"]=row.quantity
					temp_json["quality"]=row.quality
					temp_json["price"]=row.price
					response_json["deals"].append(temp_json)
		except Exception,e:

			print e
			response_json={}
			response_json["success"]=False
			response_json["message"]="user not found"
	
	except Exception,e:
		print e
		response_json={}
		response_json["success"]=False
		response_json["message"]="access token not found"
	print str(response_json)
	return JsonResponse(response_json)

			
		
@csrf_exempt
def final_deals_to_get(request):
	try:
		response_json={}	
		try:
			deal_row=deals.objects.get(product_name=str(request.POST.get("product_name")))
			setattr(dealrow,"quantity",int(request.POST.get("quantity")))
			setattr(dealrow,"quality",str(request.POST.get("quality")))
			setattr(dealrow,"price",int(request.POST.get("price")))
			deal_row.save()
			print "updated exsisting one"		
			response_json["success"]=True
			response_json["message"]="updated an exsisting deals"
		
		except:
		
			deals.objects.create(product_name=request.POST.get("product_name"),
				quantity=int(request.POST.get("quantity")),
				quality=request.POST.get("quality"),
				price=int(request.POST.get("price"))
				)
			print "new deal"		
			response_json["success"]=True
			response_json["message"]="new deal created"
	except Exception,e:
		
		print e
		response_json={}
		response_json["success"]=False
		response_json["message"]="deal not created"
	print str(response_json)
	return JsonResponse(response_json)
				






	
