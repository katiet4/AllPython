from django.shortcuts import render
from . import allSystemNumber
from LogErrors.models import ErrorsLogs
import datetime

def Systems(request):
	try:
		if request.session['security'] > 0:
			if request.POST:
				which = int(request.POST.get('system')) #int(input('(2/8/10/16): '))
				num1 = request.POST.get('NumOne')#int(input('Number one: '))
				num2 = request.POST.get('NumTwo')#int(input('Number two: '))
				Arifm = request.POST.get('PMDU')#input('(+,-,/,*): ')
				allNumbers = allSystemNumber.main(which, Arifm, num1, num2)
				return render(request, 'pageSystems.html',{'allNumbers' : allNumbers,'titles':'binarySystem'})
			return render(request, 'pageSystems.html', {'titles':'binarySystem'})
		else:
			return render(request, 'pleaseLogin.html')
	except Exception as e:
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
#def result(request):
	
# Create your views here.
