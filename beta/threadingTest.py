from threading import Thread
from time import sleep
from random import randint 
number = [False,False]
def fiveteenSeconds(name):
	sleep(int(randint(0,15)))
	if number[0] == False:
		print('i am ', name, "(1)")
		number[0] = True
	elif number[1] == False:
		print('i am ', name, "(2)")
		number[1] = True
	else:
		print('i am ', name, "(3)")
f1 = Thread(target = fiveteenSeconds, args = ("Max",))
f2 = Thread(target = fiveteenSeconds, args = ("Dred",))
f3 = Thread(target = fiveteenSeconds, args = ('Roman',))
f1.start()
f2.start()
f3.start()
