from django.shortcuts import render
from loginApp.models import Users
def login(request):
	if request.POST:
		login = request.POST.get('login')
		password = request.POST.get('password')
		try:
			if len(login)<1 or len(password)<1:
				return render(request,'login/Login.html',{'result':'Error','colors':'red'})
			CU = Users.objects.get(login=login)
			if CU.password == password:
				request.session['can'] = True
				request.session['name'] = login
				U = Users.objects.get(login = request.session['name'])
				return render(request,'mainMenu.html',{'Last_name':U.last_name,'First_name':U.first_name}) # Должен открывать сайт
			else:
				return render(request,'login/Login.html',{'result':'Error','colors':'red'})
		except Exception as e:
			return render(request,'login/Login.html',{'result':'Error','colors':'red'})
	#request.session['name'] = 'hello'
	try:
		if request.session['can']:
			U = Users.objects.get(login = request.session['name'])
			return render(request,'mainMenu.html',{'Last_name':U.last_name,'First_name':U.first_name}) # если вошел то открывать сайт
		else:
			raise Exception
	except Exception as e:
		return render(request,'login/Login.html')
	
	
def registration(request):
	if request.POST:
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		login = request.POST.get('login')
		password = request.POST.get('password')
		try:
			if len(first_name)<1 or len(last_name)<1 or len(login)<1 or len(password)<1:
				return render(request,'login/Registration.html',{'result':'Error','colors':'red'})
			CU = Users.objects.get(login=login)
			return render(request,'login/Registration.html',{'result':'Error','colors':'red'})
		except Exception as e:
			AddU = Users(first_name = request.POST.get('first_name'),
						last_name = request.POST.get('last_name'),
						login = request.POST.get('login'),
						password = request.POST.get('password'))
			AddU.save()
			return render(request,'login/Registration.html',{'result':'Succs','colors':'black'})
	#request.session['name'] = 'hello'
	return render(request,'login/Registration.html')
def exit(request):
	request.session['can'] = False
	request.session['name'] = ""
	request.session['friend'] = ''
	return render(request,'Error.html')