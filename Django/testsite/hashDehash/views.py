from django.shortcuts import render
from . import hashWords
from django.http import HttpResponse
from re import *
from LogErrors.models import ErrorsLogs
import datetime
def hashDehash(request):
	try:
		if request.session['security'] > 0:
			if request.POST:
				c = compile('(^|\s)[0-9]{1,100}($|\s)')
				key = request.POST.get('key')
				bo = c.match(key)
				if bo:
					text = request.POST.get('texts')
					texthash = request.POST.get('texthash')
					submit = request.POST.get('button')
					if submit == 'de_hash':
						text = hashWords.De_hash(key, texthash)
					else:
						texthash = hashWords.hash(key, text)
					return render(request, 'hashDehash.html', {'key': key, "text":text, 'texthash':texthash,'titles':'hash and de_hash'})
			return render(request, 'hashDehash.html',{'titles':'hash and de_hash'})
		else:
			return render(request, 'pleaseLogin.html')
	except Exception as e :
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
# Create your views here.
