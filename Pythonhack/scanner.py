from termcolor import *
import socket
import colorama
from re import *

def Scan(ports):
	hostCheckerIP = compile('(^|\s)([0-9]{1,3}\.)+([0-9]{1,3}\.)+([0-9]{1,3}\.)+[0-9]{1,3}(\s|$)')
	hostCheckerDNS = compile('(^|\s)[a-zA-Z0-9.,_-]+\.+[a-z]{2,6}(\s|$)')
	SizePorts = compile('(^|\s)[0-9]{1,5}(\s|$)')

	cprint('Host:', 'red')
	host = input()

	boolIP = hostCheckerIP.match(host)
	boolDNS = hostCheckerDNS.match(host)

	if (boolDNS or boolIP):

		for i in ports:

			boolSizePorts = SizePorts.match(str(i))

			if boolSizePorts:

				try:
					scan = socket.socket()
					scan.settimeout(0.1)
					scan.connect((host,int(i)))

				except socket.error:
					cprint(colored('Port','red') + ' --- ' +
					colored(str(i),'red') + ' --- ' +
					colored('[CLOSE]','red'))

					try:
						with open('logScanClose.txt','a') as append:
							print(str(i) + ' : [CLOSE]', file = append)

					except Exception as e:
						with open('logScanClose.txt','2') as append:
							print(str(i) + ' : [CLOSE]', file = append)
					
				else:
					cprint(colored('Port','green') + ' --- ' +
					colored(str(i),'green') + ' --- ' +
					colored('[OPEN]','green'))

					try:
						with open('logScanOpen.txt','a') as append:
							print(str(i) + ' : [OPEN]', file = append)

					except Exception as e:
						with open('logScanOpen.txt','w') as append:
							print(str(i) + ' : [OPEN]', file = append)

			else:
				cprint('Ошибка в корректности данных(Ports)','red')
				cprint('Выход...','red')

	else:
		cprint('Ошибка в корректности данных(Host)','red')
		Scan(ports)
			
def ScanALL():
	hostCheckerIP = compile('(^|\s)([0-9]{1,3}\.)+([0-9]{1,3}\.)+([0-9]{1,3}\.)+[0-9]{1,3}(\s|$)')
	hostCheckerDNS = compile('(^|\s)[a-zA-Z0-9.,_-]+\.+[a-z]{2,6}(\s|$)')
	SizePorts = compile('(^|\s)[0-9]{1,5}(\s|$)')

	cprint('Host:', 'red')
	host = input()

	boolIP = hostCheckerIP.match(host)
	boolDNS = hostCheckerDNS.match(host)

	if (boolDNS or boolIP):

		for i in range(1,65536):
			boolSizePorts = SizePorts.match(str(i))

			if boolSizePorts:

				try:
					scan = socket.socket()
					scan.settimeout(0.1)
					scan.connect((host,int(i)))

				except socket.error:
					cprint(colored('Port','red') + ' --- ' +
					colored(str(i),'red') + ' --- ' +
					colored('[CLOSE]','red'))

					try:
						with open('logScanClose.txt','a') as append:
							print(str(i) + ' : [CLOSE]', file = append)

					except Exception as e:
						with open('logScanClose.txt','2') as append:
							print(str(i) + ' : [CLOSE]', file = append)
					
				else:
					cprint(colored('Port','green') + ' --- ' +
					colored(str(i),'green') + ' --- ' +
					colored('[OPEN]','green'))

					try:
						with open('logScanOpen.txt','a') as append:
							print(str(i) + ' : [OPEN]', file = append)

					except Exception as e:
						with open('logScanOpen.txt','w') as append:
							print(str(i) + ' : [OPEN]', file = append)

			else:
				cprint('Ошибка в корректности данных(Ports)','red')
				cprint('Выход...','red')

	else:
		cprint('Ошибка в корректности данных(Host)','red')
		ScanALL()
		
	

colorama.init()

print(colored('[1]','red') + colored(' ------- Популярные порты\n','blue') +
	  colored('[2]','red') + colored(' ------- Свои порты\n','blue') +
	  colored('[3]','red') + colored(' ------- Все порты(долго)\n','blue') +
	  colored('[*]','red') + colored(' ------- Выход','blue'))

way = input()

if (way == '1'):
	ports = [	
				7, 17, 1723, 587, 2500,
				18, 20, 11, 21, 33, 22,
				23, 25, 53, 80, 110, 139,
				8000, 8080, 3128, 3389,
				6588, 1080, 5900, 8888		
											]

	Scan(ports)

elif (way == '2'):
	cprint('Ports(n1, n2, ..., nX):', 'red')
	p = input()
	Scan(p.strip().split(','))

elif (way == '3'):
	ScanALL()
	
else:
	cprint('Выход...','red')