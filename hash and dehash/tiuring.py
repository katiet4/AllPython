from math import pow,sqrt
alf = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10, 'f': 12, 'g': 14, 'h': 16, 'i': 18, 'j': 20,
		 'k': 22, 'l': 24, 'm': 26, 'n': 28, 'o': 30,
		 'p': 32, 'q': 34, 'r': 36, 's': 38, 't': 40, 'u': 42, 'v': 44, 'w': 46, 'x': 48, 'y': 50, 'z': 52,' ' : 54}
alfJust = {' ': 1, 'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23,
			 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
			 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,'z' : 101}
note = input("Note: ").strip()
key = input('Key: ').strip()
x = len(note)   #Кол-во букв и пробелов в предложени
y = 0			#Сумма всех букв и пробелов в предложении		
z = 0			#Сумма букв ключа
h = 0			#id буквы - простое число 
v = 0			#буква по счету
func = 0
#    Y
for i in note:
	y += alf[i.lower()]

#    Z
for i in key:
	z += alf[i.lower()]
words = ''
intAlf = 1
for i in note:
	h = alfJust[i]
	v = intAlf
	func = int((pow(h, 3) + pow(h, 3) + pow(x, 2) + pow(x, 2) + y + y + z + z + pow(v, 2) + pow(v, 2))/2)
	words += '|' + str(func)
	intAlf += 1
print(x, ' : ', y, ' : ', z , ' : ', h , ' : ', v)
print(words)

def dehash(noteHash,keyHash):
	note = noteHash.split('|')
	alfJust2 = {v : k for k, v in alfJust.items()}
	key = input('Key: ').strip()
	x = len(note)   #Кол-во букв и пробелов в предложени
	y = 0			#Сумма всех букв и пробелов в предложении		
	z = 0			#Сумма букв ключа
	h = 0			#id буквы - простое число 
	v = 0			#буква по счету
	func = 0
	#    Y
	for i in note:
		y += alf[i]

	#    Z
	for i in key:
		z += alf[i]
	words = ''
	intAlf = 1
	for i in note:
		v = intAlf
		func = sqrt((int(i)*2)/(pow(x, 2) + pow(x, 2) + y + y + z + z + pow(v, 2) + pow(v, 2)),3)
		h = alfJust[func]
		words += str(h)
		intAlf += 1
	print(words)
dehash(words,key)