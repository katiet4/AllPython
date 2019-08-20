from django.shortcuts import render
from UsersApp.models import Users
def login(request):
	if len(str(request))==22:
		request.session['security'] = 0
	print(request.session['security'])
	if request.POST:

		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			if Users.objects.get(email = email).password != password:
				return render(request, 'MainLog.html',{'pass':'Wrong email or password or you don`t user'})
			request.session['security'] = int(Users.objects.get(email = email).id)
			request.session['who'] = email
			return render(request, 'MainLog.html',{'pass':'Succsessful'})
		except Exception as e:
			request.session['security'] = 0
			return render(request, 'MainLog.html',{'pass':'Wrong email or password or you don`t user'})
	return render(request, 'MainLog.html')
def registration(request):
	if request.POST:
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		happyBirthdayD = request.POST.get('d')
		happyBirthdayM = request.POST.get('m')
		happyBirthdayY = request.POST.get('y')
		happyBirthday = str(happyBirthdayD) + '.' + str(happyBirthdayM) + "." + str(happyBirthdayY)
		email = request.POST.get('email')
		password = request.POST.get('password')
		Rpassword = request.POST.get('repeatpassword')
		try:
			if Users.objects.get(email = email).email == email:
				return render(request, 'MainReg.html',{'day':[i for i in range(1,32)],
					'month':[i for i in range(1,13)],
					'year':[i for i in range(1900,2019)], 'pass':'We have it email'})
		except Exception as e:
			pass
		if password != Rpassword or 8 > len(password):
			return render(request, 'MainReg.html',{'day':[i for i in range(1,32)],
				'month':[i for i in range(1,13)],
				'year':[i for i in range(1900,2019)], 'pass':'Password != Repeat password or 8 > password length'})
		else:
			U = Users(firstname = firstname,
						 lastname= lastname,
						 happyBirthday = happyBirthday, 
						 email = email, 
						 password = password,
						 security = 1)
			U.save()
			return render(request, 'MainReg.html',{'day':[i for i in range(1,32)],
				'month':[i for i in range(1,13)],
				'year':[i for i in range(1900,2019)], 'pass':'Succsessful'})
	return render(request, 'MainReg.html',{'day':[i for i in range(1,32)],
		'month':[i for i in range(1,13)],
		'year':[i for i in range(1900,2019)]})
# Create your views here.
