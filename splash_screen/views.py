from django.shortcuts import render
from django.http import JsonResponse 
from .models import *
# Create your views here.

def splash_scr_response(request):

	response_json={}
	version_row=version_data.objects.get(compulsory_update=True)
	version=version_row.version
	response_json["version"]=version
	response_json["compulsory_update"]=version_row.compulsory_update	
	
	if request.method == 'GET':
		try:
			
			fcm=str(request.GET.get("fcm"))
			if fcm!="None":
				try:
					fcm_list=fcm_data.objects.get(fcm=fcm)
					print "fcm alredy present"
					response_json["success"]=True
					response_json["message"]="fcm alredy present"
				except:
					fcm_list=fcm_data.objects.create(fcm=fcm)
					print "fcm added"
					response_json["sucess"]=True
					response_json["message"]="fcm added"
			else:
				response_json["sucess"]=True
				response_json["message"]="fcm is None"
			
		except Exception,e:

                                            
			response_json["success"]=False     
			response_json["message"]="fcm not sent"

	print str(response_json)
	return JsonResponse(response_json)

