from database import dataBase
from identification import Rand
from re import *
def Login(base,email,passwd)->'Key':
	with dataBase(base) as cursor:
		em=compile('(\s|^)[A-Za-z0-9._-]{1,100}@[a-z]{1,10}.[a-z]{0,4}(\s|$)')
		val = em.match(email)
		if val:
			_SQL = 'SELECT identificationKey FROM users WHERE (email = %s AND password = %s)'
			cursor.execute(_SQL,(email,passwd)) 
			identificationKey = cursor.fetchone()
			if identificationKey == None:
				return '0000000000000000000000000000000000000000000'
			else:
				return identificationKey[0]
		else:
			return '0000000000000000000000000000000000000000000'
"""base2 = {'host':'127.0.0.1',
		'user':'root',
		'password':'root',
		'database':'fsociety'}
p = Login(base2,'gogogo@mail.ru','gogogo228')
print(p)"""