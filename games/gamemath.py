from time import time
from random import randint

HowlongTime = input('How long time?: ')

do = input('1.  X ? X\n2.  X ? XX\n3.  X ? XXX\n4.  XX ? XX\n5.  XX ? XXX\n6.  XXX ? XXX\n')
Do = int(do)

character = input('? = (-,+,*,/): ')
TrueAnswer=999999
goodAnswer=0
badAnswer=0
allAnswer=0
results = ''
t = time()
while True:
	if(character != '-' and character != '+' and character != '*' and character != '/'):
		allAnswer = 1
		break
	END = round(time()-t)
	longTime = int(HowlongTime)
	if END>longTime:
		break
	X = randint(0,9)
	XX = randint(10,99)
	XXX = randint(100,999)
	numberOne = {
					1:X,
					2:X,
					3:X,
					4:XX,
					5:XX,
					6:XXX
							}
	X = randint(0,9)
	XX = randint(10,99)
	XXX = randint(100,999)
	numberTwo = {
					1:X,
					2:XX,
					3:XXX,
					4:XX,
					5:XXX,
					6:XXX
							}
	one = numberOne[Do]
	two = numberTwo[Do]
	normal = randint(0,1)
	if normal == 1:
		answer = input(f'{one} {character} {two}=?\n')
	else:
		answer = input(f'{two} {character} {one}=?\n')
	try:
		ans = int(answer)
	except Exception as e :
		ans = 0
	try:
		if character == '/':
			if normal == 1:
				TrueAnswer = round(one / two)
			else:
				TrueAnswer = round(two / one) 
		elif character == '+':
			if normal == 1:
				TrueAnswer = one + two
			else:
				TrueAnswer = two + one  
		elif character == '*':
			if normal == 1:
				TrueAnswer = one * two
			else:
				TrueAnswer = two * one 
		elif character == '-':
			if normal == 1:
				TrueAnswer = one - two
			else:
				TrueAnswer = two - one 
		else:
			pass
	except Exception as e:
		print('Oups!\nSorry!')
		two = 1
		if normal == 1:
			answer = input(f'{one} {character} {two}=?\n')
		else:
			answer = input(f'{two} {character} {one}=?\n')
		if character == '/':
			if normal == 1:
				TrueAnswer = one / two
			else:
				TrueAnswer = two / one 
		elif character == '+':
			if normal == 1:
				TrueAnswer = one + two
			else:
				TrueAnswer = two + one  
		elif character == '*':
			if normal == 1:
				TrueAnswer = one * two
			else:
				TrueAnswer = two * one 
		elif character == '-':
			if normal == 1:
				TrueAnswer = one - two
			else:
				TrueAnswer = two - one 
		else:
			pass
	if ans == TrueAnswer:
		goodAnswer+=1
	else:
		badAnswer+=1
	results += f'\n___________________\nArithmetic:{one} {character} {two}\nTrue answer = ' + str(TrueAnswer) +'\nYour answer = ' + str(answer)
	allAnswer+=1
procGoodAnswer=round((goodAnswer/allAnswer)*100)
procBadAnswer=round((badAnswer/allAnswer)*100)
print(results)
print('___________________\n')
print(f'good:{procGoodAnswer}%\nbad:{procBadAnswer}%')

