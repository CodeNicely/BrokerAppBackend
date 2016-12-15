from .models import keys
from pyfcm import FCMNotification

def pushnotification(device_id,message_titile,message_body):
	api_key=str(keys.objects.get(key="api_key").value)
	push_service=FCMNotification(api_key=api_key)
	result = push_service.notify_single_device(registration_id=registration_id,
		message_title=message_title,
 		message_body=message_body)

	print result

