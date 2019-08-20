from django.shortcuts import render
from . import messageVk
from re import *
from LogErrors.models import ErrorsLogs
import datetime
def message(request):

	try:
		if request.session['security'] > 0:
			if request.POST:
				c = compile('(^|\s)[0-9]{1,100}(\s|$)')
				userId = request.POST.get('id')
				message = request.POST.get('message')
				token = request.POST.get('token')
				bo = c.match(userId)
				if bo:
					resp = messageVk.mess(message, userId, token)
					return render(request, 'messageInVK.html',{'titles':'messageInVK','response':resp})
			return render(request, 'messageInVK.html',{'titles':'messageInVK'})
		else:
			return render(request, 'pleaseLogin.html')
	except Exception as e :
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()

# Create your views here.
