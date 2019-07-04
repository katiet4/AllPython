from re import *
from python import passwd
def check(First_name, Last_name, birthdayD, birthdayM, birthdayY,
						quantitly, numbers_answer, numbers, size):
	birthdayD_standart=compile('(^|\s)([0-9]{0,0}|[0-9]{2,2})$')
	birthdayM_standart=compile('(^|\s)([0-9]{0,0}|[0-9]{2,2})$')
	birthdayY_standart=compile('(^|\s)([0-9]{0,0}|[0-9]{2,2}|[0-9]{4,4})$')
	birthdayD_bool=birthdayD_standart.match(birthdayD)
	birthdayM_bool=birthdayM_standart.match(birthdayM)
	birthdayY_bool=birthdayY_standart.match(birthdayY)
	if (birthdayD_bool and birthdayM_bool and birthdayY_bool):
		return passwd(First_name, Last_name, birthdayD, birthdayM, birthdayY,
						quantitly, numbers_answer, numbers, size)
	else:
		return "ERROR"
		#Доделать таблицу,добавив оглавление и логи