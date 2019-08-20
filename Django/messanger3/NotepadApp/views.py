from django.shortcuts import render
from loginApp.models import Users
from loginApp import views
def notepad(request):
	try:
		if request.session['can'] == True:
			UN = Users.objects.get(login=request.session['name'])
			if request.POST:
				saving = request.POST.get('notepad')
				UN = Users.objects.get(login=request.session['name'])
				UN.notepad = saving
				UN.save()
				return render(request, 'notepad/notepad.html',{ 'saved' : saving })
			return render(request, 'notepad/notepad.html',{ 'saved' : UN.notepad })
		else:
			raise Exception
	except Exception as e:
		return render(request, 'Error.html')

# Create your views here.
