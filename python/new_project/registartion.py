from database import dataBase
from identification import Rand
from re import *
def Reg(base,email,passwd,twoPass):
	if passwd == twoPass:
		with dataBase(base) as cursor:
			em=compile('(\s|^)[A-Za-z0-9._-]{1,100}@[a-z]{1,10}.[a-z]{0,4}(\s|$)')
			val = em.match(email)
			if val:
				_SQL = 'INSERT INTO users(Email,password,identificationKey) VALUES( %s , %s , %s )'
				identificationKey = Rand()
				s  = str(identificationKey)
				cursor.execute(_SQL,(email,passwd,s))
				return identificationKey
			else:
				return '0000000000000000000000000000000000000000000'
	else:
		return '0000000000000000000000000000000000000000000'
"""base2 = {'host':'127.0.0.1',
		'user':'root',
		'password':'root',
		'database':'fsociety'}
p = Reg(base2,'anton1678_@mail.ru','asdsd')
print(p)"""