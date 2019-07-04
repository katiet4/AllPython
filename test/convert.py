from random import randint
import pprint

def convertsFunc(number = 0,math = 0,numberConvert = 0):
	mass = set()
	math = 0
	copy=[]
	OPEN = 1
	intCopy = int(len(copy))
	if numberConvert == 1:
		mass.add('()')
	elif numberConvert == 2:
		mass.add('()()')
		mass.add('(())')
	else:
		while math < number :
			if intCopy == 0:
				copy.append('(') 
			ran = randint(0,1)
			if ran == 0:
				copy.append('(')
				OPEN+=1
			else:
				copy.append(')')
				OPEN-=1
			intCopy = int(len(copy))
			if intCopy == numberConvert:
				for i in range(0,numberConvert-1):
					ran = randint(0,1)
					if ran == 0:
						copy.append('(')
						OPEN+=1
					else:
						copy.append(')')
						OPEN-=1
				copy.append(')')
				OPEN-=1
				String = ''.join(copy)
				Cls = ['(()','(()()','((()','(((()','(()()()','((()()','(((()()','(()()()()','((()()()','(((()()()','(()()()()()','((()()()()','(((()()()()','(()()()()()()','((()()()()()','(((()()()()()','(()()()()()()()','((()()()()()()','(((()()()()()()','(()()()()()()()()','((()()()()()()()','(((()()()()()()()',
														'((())','((((()','(((((()','((((()()','((((((()','(((((()()','(((((((()','((((()()()','((((((()()','((((((((()','(((((()()()','(((((((()()','(((((((((()'	,'((((()()()()','((((((()()()','((((((((()()','((((((((((()','(((((()()()()','(((((((()()()','(((((((((()()','(((((((((((()',')(()']
				op = ['())','()())','()))','())))','()()())','()()))','()())))','()()()())','()()()))','()()())))','()()()()())','()()()()))','()()()())))','()()()()()())','()()()()()))','()()()()())))','()()()()()()())','()()()()()()))','()()()()()())))','()()()()()()()())','()()()()()()()))','()()()()()()())))',
														'(()))','()))))','())))))','()()))))','()))))))','()())))))','())))))))','()()()))))','()()))))))','()))))))))','()()())))))','()())))))))','())))))))))'	,'()()()()))))','()()()))))))','()()))))))))','()))))))))))','()()()())))))','()()())))))))','()())))))))))','())))))))))))','())(']
				bo = False
				intbo = 0
				for i in range(0, int(numberConvert/2)):
					if String[0:numberConvert-i] not in op and String[numberConvert+i:int(numberConvert*2)] not in Cls:
						intbo += 1
				if intbo == int(numberConvert/2):
					bo = True
				if (OPEN == 0 and bo):
					mass.add(String)
					math+=1
					print(math)
				copy.clear()
				OPEN = 1
			intCopy = int(len(copy))
	return (len(mass),mass)

numberConvert = int(input('How long converts? : '))

converts = numberConvert
if converts <= 5:
	n,k = convertsFunc(number=10000, numberConvert = numberConvert)
elif converts <= 10:
	n,k = convertsFunc(number=100000, numberConvert = numberConvert)
elif converts <= 20:
	n,k = convertsFunc(number=500000, numberConvert = numberConvert)
else :
	n,k = convertsFunc(number=1000000, numberConvert = numberConvert)
pprint.pprint(k)
pprint.pprint(n)