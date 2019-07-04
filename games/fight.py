""" 
0 - helths
1 - power
2 - strong
"""
def Enemy():
	try:
		pointsEnemy = input('Points enemy:')
		for i in range(0,int(pointsEnemy)):
			ran = randint(0,3)
			enemy[ran] += 1
	except Exception as e:
		print('\n','Error: points enemy:(Integer)','\n')
		Enemy()
def You():
	try:
		YourPoints = input('Your points:')
		characteristicsMyPerson(int(YourPoints))
	except Exception as e:
		print('\n','Error: your points:(Integer)','\n')
		You()
	
	
	
def characteristicsMyPerson(points):
	if points == 0:
		return
	print('Your characteristics:','\n','helths:',myPerson[0],
		'\n','power:',myPerson[1],'\n','strong:',myPerson[2],'\n',
		'intellect:',myPerson[3],'\n')
	print('Points : ',points)
	print(' 0.helths')
	print(' 1.power')
	print(' 2.strong')
	print(' 3.intellect')
	character = input('(Number):(Points) : ')
	characters = character.split(':')
	try:
		if int(characters[1]) > points:
			print('You don`t have as points')
			characteristicsMyPerson(points)
	except Exception as e:
		print('\n','Error: introduse (!!! (Number):(Points) !!!)','\n')
		characteristicsMyPerson(points)
	myPerson[int(characters[0])] += int(characters[1])
	characteristicsMyPerson(points - int(characters[1]))
from random import randint 
enemy = [5,1,1,1]
myPerson = [5,1,1,1]
print('Setup:')
Enemy()
You()
print('Your characteristics:',', helths:',myPerson[0],
		', power:',myPerson[1],', strong:',myPerson[2],
		', intellect:',myPerson[3],'\n')
print('Characteristics your enemy:',', helths:',enemy[0],
		', power:',enemy[1],', strong:',enemy[2],
		', intellect:',enemy[3],'\n')
cofEnemy = int(((enemy[1]*enemy[3])+(enemy[2]*enemy[3]))/2)
cofMyPerson = int(((myPerson[1]*myPerson[3])+(myPerson[2]*myPerson[3]))/2)
while True:
	if enemy[0] == 0:
		print('\n','You won!')
		break
	elif myPerson[0] == 0:
		print('\n','You lost!')
		break
	ranEnemy = randint(0,cofEnemy)
	ranMyPerson = randint(0,cofMyPerson)
	if ranMyPerson > ranEnemy:
		enemy[0] -= 1
	elif ranMyPerson < ranEnemy:
		myPerson[0] -= 1
	else:
		continue
	print('\n','My person helths: ',myPerson[0],'\n',
			'My enemy helth: ',enemy[0],'\n')
	input('	Click to continue...')
