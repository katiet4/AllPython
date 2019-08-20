from django.shortcuts import render
from . import RSA
def RsA(request):
	try:
		if request.session['can'] == True:
			if request.POST:
				what = request.POST.get('what')
				if what == 'encrypting':
					message = request.POST.get('decrypt')
					d = request.POST.get('d')
					try:
						n = int(request.POST.get('n'))
						e = int(request.POST.get('e'))
					except Exception as e:
						return render(request,'EncDec.html')
					encrypt = RSA.enc(message,e,n)
					return render(request,'EncDec.html',{'encrypt' : encrypt,'e': e,'n':n,'d':d})
				elif what == 'decrypting':
					message = request.POST.get('encrypt')
					e = request.POST.get('e')
					try:
						n = int(request.POST.get('n'))
						d = int(request.POST.get('d'))
					except Exception as e:
						return render(request,'EncDec.html')
					decrypt = RSA.dec(message,d,n)
					return render(request,'EncDec.html',{'decrypt' : decrypt,'d': d,'n':n,'e':e})
				else:
					everything = RSA.keys()
					return render(request,'EncDec.html',{
														'd': everything['close'][1],
														'n':everything['open'][0],
														'e':everything['open'][1]})
			return render(request,'EncDec.html')
		else:
			raise Exception
	except Exception as e:
		return render(request, 'Error.html')
# Create your views here.
