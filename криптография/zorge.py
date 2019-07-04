from math import ceil
from random import randint
Mabc = {}
abc = "abcdefghijklmnopqrstuvwxyz./"

FrequentLetters = "asintoer"

WordIsKey = input("Input Key: ")
Igamm = int(input("input gamm: "))

FirstColumns = len(WordIsKey)
FirstRows = int(ceil(28/FirstColumns))

FirstTable = [[] for i in range(FirstRows)]

index = 1

for i in range(FirstColumns):
	FirstTable[0].append(WordIsKey[i])
for i in range(len(abc)):
	if len(FirstTable[index]) == FirstColumns:
		index+=1
	if abc[i] not in FirstTable[0]:
		FirstTable[index].append(abc[i])

SecondColumns = 10
SecondRows = int(ceil((28 - len(FrequentLetters)) / SecondColumns))+1

SecondTable = [[] for i in range(SecondRows)]

for x in range(FirstColumns):
	for y in range(FirstRows):
		try:
			if FirstTable[y][x] in FrequentLetters:
				SecondTable[0].append(FirstTable[y][x])
		except Exception as e:
			pass

index = 1
for x in range(FirstColumns):
	for y in range(FirstRows):
		if len(SecondTable[index]) == SecondColumns:
			index+=1
		try:
			if FirstTable[y][x] not in SecondTable[0]:
				SecondTable[index].append(FirstTable[y][x])	
		except Exception as e:
			pass
for y in range(SecondRows):
	for x in range(SecondColumns):
		try:
			if y == 0:
				Mabc[SecondTable[y][x]] = str(x)
			else:
				Mabc[SecondTable[y][x]] = str(10-(len(SecondTable)-y))+str(x) 
		except Exception as e:
			pass
gamm = [746, 402, 688, 918, 385, 159, 216, 102, 186, 619, 279, 626, 3, 897, 33, 281, 261, 432, 383, 666, 553,
		931, 759, 461, 145, 920, 580, 178, 65, 545, 486, 48, 992, 777, 795, 199, 828, 475, 474, 116, 995, 987, 236,
 		550, 816, 80, 408, 284, 986, 388, 426, 913, 746, 806, 601, 831, 18, 47, 812, 101, 838, 496, 294, 293, 463,
 		454, 780, 511, 930, 479, 753, 336, 883, 947, 330, 760, 637, 44, 933, 871, 22, 268, 100, 307, 624, 731, 333,
   		73, 88, 64, 348, 482, 734, 270, 929, 144, 817, 147, 485, 175]
HashOrDehash = input("Hash or dehash?(1/0): ")
if HashOrDehash == "1":	
	text = input("Text: ").lower()
	end = ''
	for i in text:
		if i == ' ':
			continue
		end+=Mabc[i]
	text1 = ''
	howlong = 1

	index = 0
	maybe = ""
	lenS = len(Mabc['/'])

	for i in range(len(text)):
		if text[i] == ' ':
			continue
		r = randint(0,1)
		if r == 0:
			r = randint(0,1)
			if r == 0:
				text1 += Mabc[text[i]] + Mabc['/']
			else:
				text1 += Mabc['/'] + Mabc[text[i]]
		else:
			text1 += Mabc[text[i]]
	count=0
	end = ''
	for i in range(len(text1)):
		count+=1
		end+=text1[i]
		if count == 5:
			end += " "
			count = 0
	check = end.strip().split(" ")
	if len(check[-1]) < 5:
		check.pop(-1)
	end2 = ""
	for i in check:
		if Igamm>=len(gamm):
			Igamm = 0
		if i[0] == "0":
			end2 += "0"+str(int(i)+gamm[Igamm])+" "
		else:
			end2 += str(int(i)+gamm[Igamm])+" "
		Igamm+=1
	print(end2)

	

else:
	end2 = input("input Hash: ")
	end = ""
	for i in end2.strip().split(" "):
		if Igamm>=len(gamm):
			Igamm = 0
		if i[0] == "0":
			end += "0"+str(int(i)-gamm[Igamm])
		else:
			end += str(int(i)-gamm[Igamm])
		Igamm+=1
	RMabc = {}
	for k,v in Mabc.items():
		RMabc[v] = k
	answ = ""
	index = 0
	while index < len(end):
		if end[index] == ' ':
			index+=1
			continue
		#print(end[index])
		if end[index] in RMabc:
			answ += RMabc[end[index]]
			index+=1
		else:
			try:
				if end[index+1] == " ":
					mb = RMabc[end[index]+end[index+2]]
					index+=3
				else:
					mb = RMabc[end[index]+end[index+1]]
					index+=2
				if mb == '/':
					answ+=''
				else:
					answ+=mb
			except Exception as e:
				index+=1
			
	print(answ)