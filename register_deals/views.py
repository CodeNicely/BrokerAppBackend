from django.shortcuts import render
from .models import *
import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login.models import *
# Create your views here.
@csrf_exempt
def register_offer(request):
	
	try:

		access_token=request.POST.get("access_token")
		json=jwt.decode(str(access_token),'999123',algorithms=['HS256'])
		print json["mobile"]
		response_json={}
		offers.objects.create(mobile=int(json["mobile"]),
			product_name=request.POST.get("product_name"),
			quantity=int(request.POST.get("quantity")),
			quality=request.POST.get("quality"),
			price=int(request.POST.get("price")),
			catigory=request.POST.get("catigory"))
		response_json['success']=True
		response_json["message"]="offer saved"

	except Exception,e:

		print e
		response_json={}
		response_json["success"]=False
		response_json["message"]="offer not saved. Try again"

	print str(response_json)
	return JsonResponse(response_json)


@csrf_exempt
def send_offers(request):
	
	try:
		response_json={}
		response_json["success"]=True
		response_json["message"]="all unsent offer sent"
		response_json["offers"]=[]
		for offer_row in offers.objects.filter(is_sent=False):
			offer_row.is_sent=True
			offer_row.save()
			temp_json={}
			
			user_row=login_user.objects.get(mobile=offer_row.mobile)
			temp_json["name"]=user_row.name
			temp_json["firm_name"]=user_row.firm_name
			temp_json["mobile"]=user_row.mobile
			temp_json["product_name"]=offer_row.product_name
			temp_json["quality"]=offer_row.quality
			temp_json["price"]=offer_row.price
			temp_json["quantity"]=offer_row.quantity
			response_json['offers'].append(temp_json)
			
	except Exception,e:
		
		print e
		response_json={}
		response_json["success"]=False
		response_json["message"]="offers not sent"

	print str(response_json)
	return JsonResponse(response_json)
							

	







