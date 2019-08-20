from django.shortcuts import render
from LogErrors.models import ErrorsLogs
def logplease(request):
	if request.session['security'] > 0:
		return render(request, 'Logs.html', {'object_list' : ErrorsLogs.objects.all().order_by('-id')})
	else:
		return render(request, 'pleaseLogin.html')
# Create your views here.
