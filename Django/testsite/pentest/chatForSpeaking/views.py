from django.shortcuts import render
from chatForSpeaking.models import ChatBD
import datetime
def chatDef(request):
	if request.session['security'] > 0:
		if request.POST:
			what = request.POST.get('message')
			who = request.session['who']
			when = str(datetime.datetime.today())
			c = ChatBD(what = what, who = who, when = when)
			c.save()
		return render(request, 'chat.html', {'objects' : ChatBD.objects.all().order_by('-id')})
	else:
		return render(request, 'pleaseLogin.html')
# Create your views here.
