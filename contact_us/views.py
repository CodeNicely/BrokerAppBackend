from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from login.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
import jwt
from custom.sms import send_sms

@csrf_exempt
def contact_us(request):
	response_json={}	
	if request.method=='GET':
		response_json['success']=True
		response_json['message']="Successful"
		response_json['firm_name']="Agrawal Brothers"
		response_json['address']="Agrawal Brothers , Ramayan Complex Ramsagarpara , Raipur ( C.G ) - 492001"
		response_json['mobile1']="+91 9425503905"
		response_json['mobile2']="+91 9406202298"
		response_json['mobile3']="+91 9300293177"
		response_json['landline1']="0771 2292212"
		response_json['landline2']="0771 2292237"
	else:
		response_json['success']=False
		response_json['message']="I am a big hacker , Please Get Out of Here!"	
	return JsonResponse(response_json)

