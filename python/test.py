#16
inpu = input('Number: ')
_2 = ''
t = inpu.split('.')
code = {
	'10':'A',
	'11':'B',
	'12':'C',
	'13':'D',
	'14':'E',
	'15':'F',
	'16':'G'
	}
num = int(t[0])
while (num>=16):
	one = (num%16)
	if one > 9:
		string = str(one)
		_2+=code[string]
	else:
		_2+=str((num%16))
	num/=16
	num=int(num)
_2+=str(num)
_16end = ''
back = -1	
for i in _2:
	_16end+=_2[back]
	back-=1
print(_16end)

lengtharr = len(t)
if lengtharr==1:
	t.append('0')
if t[1]=='':
	t[1]='0'
theend = ''
length = len(t[1])
numstr=int(t[1])
numster = '1'+('0'*length)
numsterint= int(numster)
test = numstr/numsterint
endint = test
for i in range(length):
	summ=(endint*16)
	end = int(summ)
	if end != 0:
		if end >=10:
			number = str(end)
			r = code[number]
			theend+=str(r)
		else:
			theend+=str(end)
		endint = summ-end
	else:
		theend+=str(end)
		endint = summ
if theend == '':
	theend = '0'
Theend = _16end+'.'+theend
self._16.text=Theend







#8
"""inpu = input('Number: ')
_2 = ''
t = inpu.split('.')
num = int(t[0])
while (num>=8):
	_2+=str((num%8))
	num/=8
	num=int(num)
_2+=str(num)
_8end = ''
back = -1	
for i in _2:
	_8end+=_2[back]
	back-=1
lengtharr = len(t)
if lengtharr==1:
	t.append('0')
if t[1]=='':
	t[1]='0'
theend = ''
length = len(t[1])
numstr=int(t[1])
numster = '1'+('0'*length)
numsterint= int(numster)
test = numstr/numsterint
endint = test
for i in range(length):
	summ=(endint*8)
	end = int(summ)
	if end != 0:
		theend+=str(end)
		endint = summ-end
	else:
		endint = summ
if theend == '':
	theend = '0'
Theend = _8end+'.'+theend
self._2.text=Theend
"""











"""endtwo = ''
two = ''
length = len(t[1])
numstr=int(t[1])
numster = '1'+('0'*length)
numsterint= int(numster)
test = str(numstr/numsterint)
num2=float(test)
for i in range(length):
	integet = round(num2)
	if (integet == 1):
		two+='1'
	else:
		two+='0'
	print(num2)
	num2 = float(num2*2)
print(_2end,'.',two)"""