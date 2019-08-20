from django.shortcuts import render
from . import border
from re import *

from LogErrors.models import ErrorsLogs
import datetime
def Borders(request):
	try:
		if request.session['security'] > 0:
			if request.POST:
				c = compile('(^|\s)[0-9]{1,100}($|\s)')
				howlongs = request.POST.get('howLong2')
				print(howlongs)
				bo = c.match(howlongs)
				if bo :
					arr = border.bord(int(howlongs))
					return render(request,'borders.html',{'itog' : arr,'titles':'borders'})
			return render(request,'borders.html',{'titles':'borders'})
		else:
			return render(request, 'pleaseLogin.html')
	except Exception as e:
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
# Create your views here.
