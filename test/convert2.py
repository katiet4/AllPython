def convertsFunc(count,leftRem,rightRem,index):
	print(leftRem,':',rightRem)
	if(leftRem < 0 or rightRem < leftRem):
		return
	if leftRem == 0 and rightRem == 0:
		mass.add(''.join(Str))
		leftRem = count
		rightRem = count
		Str.clear()
	else:

		Str.append('(')
		convertsFunc(count,leftRem-1,rightRem,index+1)
		Str.append(')')
		convertsFunc(count,leftRem,rightRem-1,index+1)

numberConvert = int(input('How long converts? : '))
count = int(numberConvert)
mass = set()
Str = []
convertsFunc(count,count,count,0)
print(mass)