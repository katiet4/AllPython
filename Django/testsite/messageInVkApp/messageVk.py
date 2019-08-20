import requests
from LogErrors.models import ErrorsLogs
import datetime
def mess(message, userId, token):
	try:
		resp = requests.get("https://api.vk.com/method/messages.send?user_id="+userId+"&message="+message+"&access_token="+ token +"&v=5.87")
		return resp
	except Exception as e :
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()

