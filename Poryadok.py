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
def deistv(arr):
	for i in arr:
	    z = 0
	    for i in arr:
	        if(i == '/'):
	            z += 1
	            key = arr.index(i)
	            k = float(arr[key-1])/float(arr[key+1])
	            print(str(float(arr[key-1]))+"/"+str(float(arr[key+1]))+"="+str(float(arr[key-1])/float(arr[key+1])))
	            arr[key-1] = str(k)
	            arr.pop(key)
	            arr.pop(key)
	    if(z == 0):
	        break

	for i in arr:
	    z = 0
	    for i in arr:
	        if(i == '*'):
	            z += 1
	            key = arr.index(i)
	            k = float(arr[key-1])*float(arr[key+1])
	            print(str(float(arr[key-1]))+"*"+str(float(arr[key+1]))+"="+str(float(arr[key-1])*float(arr[key+1])))
	            arr[key-1] = str(k)
	            arr.pop(key)
	            arr.pop(key)
	    if(z == 0):
	        break


	for i in arr:
	    z = 0
	    for i in arr:
	        if(i == '-'):
	            z += 1
	            key = arr.index(i)
	            k = float(arr[key-1])-float(arr[key+1])
	            print(str(float(arr[key-1]))+"-"+str(float(arr[key+1]))+"="+str(float(arr[key-1])-float(arr[key+1])))
	            arr[key-1] = str(k)
	            arr.pop(key)
	            arr.pop(key)
	    if(z == 0):
	        break


	for i in arr:
	    z = 0
	    for i in arr:
	        if(i == '+'):
	            z += 1
	            key = arr.index(i)
	            k = float(arr[key-1])+float(arr[key+1])
	            print(str(float(arr[key-1]))+"+"+str(float(arr[key+1]))+"="+str(float(arr[key-1])+float(arr[key+1])))
	            arr[key-1] = str(k)
	            arr.pop(key)
	            arr.pop(key)
	    if(z == 0):
	        break
	return arr[0]
def concatination(stringNomber,stringSc, iNum):
	stringScLenght = len(stringSc)
	finish = stringSc
	for i in range(len(stringSc) - len(iNum)):
		if stringSc[i:i+len(iNum)] == iNum:
			finish = stringSc[0:i-1] + stringNomber + stringSc[i+len(iNum)+1:]
			break
	return finish
def split2(string):
	end = []
	active = False
	Open = 0
	STR = ""
	for i in string:
		if i == '(':
			active = True
			Open+=1
		elif i == ")":
			Open-=1
			if Open == 0:
				active = False
				end.append(STR[1:])
				STR = ""
		if active:
			STR+=i
	return end

def parsing(string):

	if "(" in string:
		for i in split2(string):
			try:
				nomber = str(round(float(parsing(i))))
			except Exception as e:
				return "break"
			st = concatination(nomber,a[0],i)
			a[0] = st
			return "break"
	else:
		s = deistv(split4(string))
		return s

v = input('Value: ')
a = [v]
num = "break"
while ('break' in num):
	num = parsing(a[0])