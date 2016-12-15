from django.shortcuts import render
from django.http import JsonResponse
from login.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
import jwt
from custom.sms import send_sms
# Create your views here.
@csrf_exempt
def send_otp(request):
	
	if request.method=='POST':
	   response_json={}
	   try:		
		name=str(request.POST.get("name"))
		firm_name = str(request.POST.get("firm_name"))
		mobile=str(request.POST.get("mobile"))
		city=str(request.POST.get("city"))
		catigory=str(request.POST.get("catigory"))
		otp=random.randint(10000,99999)
		#opt sending
		msg="your one time otp is "+str(otp);		
		send_sms(mobile,msg)
		
		try:
			otp_row=otp_info.objects.get(mobile = int(mobile))
			setattr(otp_row,'flag',False)
			setattr(otp_row,'otp',int(otp))
			otp_row.save()
			user_row=login_user.objects.get(mobile=int(mobile))
			setattr(user_row,'name',name)
			setattr(user_row,'firm_name',firm_name)
			setattr(user_row,'city',city)
			setattr(user_row,'catigory',catigory)
			user_row.save()
			print "old user"

		except:
			otp_info.objects.create(mobile=int(mobile),otp=int(otp))
			login_user.objects.create(name=name,
				firm_name=firm_name,
				city=city,
				mobile=int(mobile),
				catigory=catigory)
			print "new user created"
		response_json['success']=True
		response_json['message']="Otp Sent Successfully"
	   except Exception,e:
		print e
		response_json['success']=False
		response_json['message']="Otp is not sent"
	   print str(response_json)
	   return JsonResponse(response_json)
	else:
		print "request not post"
		response_json={}
		response_json['success']=False
		response_json['message']="request not post"
		return JsonResponse(response_json)	   

@csrf_exempt
def verify_otp(request):
	
	response_json={}
	try:
		mobile=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))
		access_token='No Access Token'
		otp_list=otp_info.objects.get(mobile=int(mobile))
		

		if otp_list.otp == int(otp):
			
			try:
				setattr(otp_list,'flag',True)
				access_token= jwt.encode({'mobile':str(mobile)}, '999123',algorithm='HS256')
				setattr(otp_list,'access_token',access_token)
				otp_list.save()
				response_json['access_token']=str(access_token)
				print 'Access Token Created'
				response_json['success']=True
				response_json['message']='Successful'
			except Exception,e:
				response_json['access_token']='None'
				print e
				response_json['success']=False
				response_json['message']='Unable to create Access Token'
			

		else:
			response_json['success']=False
			response_json['message']='Invalid Otp'
	except Exception,e:
		response_json['success']=False
		response_json['message']='Invalid Mobile Number'
		print e
	print str(response_json)
	return JsonResponse(response_json)
			







			
