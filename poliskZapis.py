def split4(v):
    arr2 = list(v)
    k = 0
    for i in range(0,len(arr2)):
        if(arr2[k] == '+') or (arr2[k] == '-') or (arr2[k] == '/') or (arr2[k] == '*') or (arr2[k] == '(') or (arr2[k] == ')'):
            arr2.insert(k,'|')
            arr2.insert(k+2,'|')
            k+=1
        k+=1
    arr2 = list(reversed(arr2))
    #-------------------------------
    k = 0
    for i in range(0,len(arr2)):
        if(arr2[k] == '+') or (arr2[k] == '-') or (arr2[k] == '/') or (arr2[k] == '*') or (arr2[k] == '(') or (arr2[k] == ')'):
            arr2.insert(k,'|')
            arr2.insert(k+2,'|')
            k+=1
        k+=1
    arr2 = list(reversed(arr2))
    #------------------------------
    stroka = ''.join(arr2)
    arr2 = stroka.split('|')
    #------------------------------
    k = 0
    for i in arr2:
        if(i == ''):
            arr2.remove(arr2[k])
        k+=1
    arr2 = list(reversed(arr2))
    #------------------------------
    k = 0
    for i in arr2:
        if(i == ''):
            arr2.remove(arr2[k])
        k+=1
    arr2 = list(reversed(arr2))
    return arr2
def colk(znak,one,two):
	if znak == "+":
		StackWithNumber.append(one+two)
	elif znak == "-":
		StackWithNumber.append(one-two)
	elif znak == '*':
		StackWithNumber.append(one*two)
	else:
		StackWithNumber.append(round(one/two))
v = input('Value: ')
arr2 = split4(v)
priority = {'+':1,'-':1,'*':2,'/':2,'(':0}
StackWithNumber = []
StackWithZnak = []
for i in arr2:
	if i == '+' or i == '-' or i == '*' or i == '/' or i == '(' or i == ')':
		if len(StackWithZnak) == 0:
			StackWithZnak.append(i)
		else:
			if i == '(':
				StackWithZnak.append(i)
			elif i == ')':
				for i2 in range(-1,len(StackWithZnak)*(-1)-1,-1):
					if StackWithZnak[-1] == '(':
						StackWithZnak.pop(-1)
						break
					else:
						znak = StackWithZnak.pop(-1)
						one = int(StackWithNumber.pop(-2))
						two = int(StackWithNumber.pop(-1))
						colk(znak,one,two)

			elif priority[StackWithZnak[-1]]<priority[i]:
				StackWithZnak.append(i)
			else:
				znak = StackWithZnak.pop(-1)
				one = int(StackWithNumber.pop(-2))
				two = int(StackWithNumber.pop(-1))
				StackWithZnak.append(i)
				colk(znak,one,two)
	else:
		StackWithNumber.append(i)
	# print(StackWithNumber)
	# print(StackWithZnak)
for i2 in range(-1,len(StackWithZnak)*(-1)-1,-1):
	znak = StackWithZnak.pop(-1)
	one = int(StackWithNumber.pop(-2))
	two = int(StackWithNumber.pop(-1))
	colk(znak,one,two)
print(StackWithNumber[0])
