from django.shortcuts import render
from UsersApp.models import Users
from chatWithFriends.models import DialogueBD, DialoguesBD
import datetime
def Friends(request):
	if request.session['security'] > 0:
		Iam = request.session['who']
		arrayFriends = []
		if request.POST:
			find = request.POST.get('nameOFfind')
			button = request.POST.get('button')
			if button == 'Go find':
				for i in Users.objects.all():
					if find in i.email and Iam != i.email:
						arrayFriends.append(i)
				return render(request, 'friends.html',{'friends':arrayFriends})
			else:
				Iam = request.session['who']
				friend = request.POST.get('button')
				try:
					D = DialoguesBD.objects.get(who = Iam + ' && ' + friend).id
				except Exception as e:
					D = DialogueBD(who = Iam + ' && ' + friend, what = '', when = '')
					D.save()
					D = DialogueBD(who = friend + ' && ' + Iam, what = '', when = '')
					D.save()
					Ds = DialoguesBD(who = Iam + ' && ' + friend, which = str(D))
					Ds.save()
					Ds = DialoguesBD(who = friend + ' && ' + Iam, which = str(D))
					Ds.save()
				arrayFriends = []
				for i in Users.objects.all():
					if Iam != i.email:
						arrayFriends.append(i)
				return render(request, 'friends.html',{'friends':arrayFriends, 'pass' : 'Add Succsessful'})
		for i in Users.objects.all():
				if Iam != i.email:
					arrayFriends.append(i)
		return render(request, 'friends.html',{'friends':arrayFriends})
	else:
		return render(request, 'pleaseLogin.html')

# Create your views here.

def Dialogues(request):
	if request.session['security'] > 0:
		arr = []
		Iam = request.session['who']
		if request.POST:
			button = request.POST.get('button')
			if button == 'update':
				for i in DialogueBD.objects.all().order_by('-id'):
					if str(i.who).startswith(Iam) and str(i.what) != '' and str(i.who).endswith(request.session['friend']):
						arr.append(i)
			elif button == 'Send':
				message = request.POST.get('message')
				D = DialogueBD(who = Iam + ' && ' + request.session['friend'], what = Iam + ':' + message, when = str(datetime.datetime.today()))
				D.save()
				D = DialogueBD(who = request.session['friend'] + ' && ' + Iam,what = Iam + ':' + message, when = str(datetime.datetime.today()))
				D.save()
				for i in DialogueBD.objects.all().order_by('-id'):
					if str(i.who).startswith(Iam) and str(i.what) != '' and str(i.who).endswith(request.session['friend']):
						arr.append(i)
			elif button == 'Go find':
				find = request.POST.get('nameOFfind')
				for i in DialoguesBD.objects.all():
					if find in i.who and str(i.who).startswith(Iam):
						arr.append(i)
				return render(request, 'dialogues.html',{'dialogues':arr})
			else:
				p = button.split(' && ')
				request.session['friend'] = p[1]
				for i in DialogueBD.objects.all().order_by('-id'):
					if str(i.who).startswith(Iam) and str(i.what) != '' and str(i.who).endswith(request.session['friend']):
						arr.append(i)
			return render(request, 'dialogue.html',{'dialogues':arr})
		for i in DialoguesBD.objects.all():
			print(i.who)
			if str(i.who).startswith(Iam):
				print('hello')
				arr.append(i)
		return render(request, 'dialogues.html',{'dialogues':arr})
	else:
		return render(request, 'pleaseLogin.html')

