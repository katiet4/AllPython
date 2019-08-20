from django.shortcuts import render
from loginApp.models import Users
from messagesApp.models import Messages

def dialogs(request):
	try:
		if request.POST:
			try:
				withWho = request.POST.get('U')
				if withWho == None:
					raise Exception
				try:
					request.session['friend'] = withWho
					DU = Messages.objects.get(who = request.session['name']+"&&"+withWho)
					return render(request, 'message/Dialog.html',{'saved':DU.dialog})
				except Exception as e:
					DU = Messages(who = request.session['name']+"&&"+withWho, dialog = '')
					DU2 = Messages(who = withWho+"&&"+request.session['name'], dialog = '')
					DU.save()
					DU2.save()
					request.session['friend'] = withWho
					return render(request, 'message/Dialog.html')
			except Exception as e:
				update = request.POST.get('update')

				if update != None:
					DU = Messages.objects.get(who = request.session['name']+"&&"+request.session['friend'])
					return render(request, 'message/Dialog.html',{'saved':DU.dialog})
				sending = request.POST.get('message')

				if len(sending) < 1 :
					DU = Messages.objects.get(who = request.session['name']+"&&"+request.session['friend'])
					return render(request, 'message/Dialog.html',{'saved':DU.dialog})

				DU = Messages.objects.get(who = request.session['name']+"&&"+request.session['friend'])
				DU2 = Messages.objects.get(who = request.session['friend']+"&&"+request.session['name'])
				D = DU.dialog + '\n' +request.session['name']+" : "+ sending

				DU.dialog = D
				DU2.dialog = D

				DU.save()
				DU2.save()
				DU = Messages.objects.get(who = request.session['name']+"&&"+request.session['friend'])
				return render(request, 'message/Dialog.html',{'saved':DU.dialog})
		return render(request, 'message/Dialogs.html',{'users':Users.objects.all(),'me':request.session['name']})
	except Exception as e:
		print(e)
		return render(request, 'Error.html')
# Create your views here.
