from database import dataBase
from identification import Rand
def Aunt(base,identificationKey,Email):
	with dataBase(base) as cursor:
		_SQL = 'SELECT id FROM users WHERE (identificationKey = %s AND Email = %s)'
		s = str(identificationKey)
		cursor.execute(_SQL,(s,Email))
		what = cursor.fetchone()
		integer = int(what[0])
		if ((integer % 2) == 0):
			booling = True
		else:
			booling = False
	return booling