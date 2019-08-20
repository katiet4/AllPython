from random import randint
from LogErrors.models import ErrorsLogs
import datetime
def bord(borders):
	try:
		num = borders - 1
		openedBorder = num
		closedBorder = num
		allReal = set()
		EndString = ''
		end = pow(2, openedBorder+closedBorder)
		while end != int(len(allReal)):
			EndString += '('
			for i in range(0,(openedBorder+openedBorder)):
				r = randint(0,1)
				if r == 1 :
					EndString += '('
					openedBorder -= 1
				else:
					EndString += ')'
					closedBorder -= 1
			EndString += ')'
			allReal.add(EndString)
			openedBorder = num
			closedBorder = num
			EndString = ''
		endArr = []
		openedBorder = 0
		closedBorder = 0
		for i in allReal:
			openedBorder = 0
			closedBorder = 0
			for r in range(0, borders):
				if i[r] == ')':
					closedBorder += 1
				else:
					openedBorder += 1
			if closedBorder > openedBorder:
				continue
			for r in range(borders, int(len(i))):
				if i[r] == '(':
					closedBorder -= 1
				else:
					openedBorder -= 1
			if closedBorder == 0 and openedBorder == 0:
				if (i[0]+i[1]+i[2]) != '())' and (i[-3]+i[-2]+i[-1]) != '(()':
					endArr.append(i)
		check = '('
		"""
		for i in range(1, int(borders/2)+1):
			for r in range(0, i):"""	
		return endArr
	except Exception as e:
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
		pass
