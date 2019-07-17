arr = input("Array: ").split(',')
arr2 = [[i2 for i2 in i] for i in arr]
print(arr2)
Max = int(arr2[0][0])
MaxIndex = 0
endString = ''
whatDo = True
while True:
	for i in range(len(arr2)):
		if int(arr2[i][0]) > Max:
			Max = int(arr2[i][0])
			MaxIndex = i
		elif int(arr2[i][0]) == Max:
			if len(arr2[MaxIndex]) > len(arr2[i]):
				for i2 in range(len(arr2[i])):
					if arr2[i][i2]>arr2[MaxIndex][i2]:
						Max = int(arr2[i][0])
						MaxIndex = i
						whatDo = False
						break
					elif arr2[i][i2]<arr2[MaxIndex][i2]:
						whatDo = False
						break
				if whatDo:
					Max = int(arr2[i][0])
					MaxIndex = i
				whatDo = True
	endString += ''.join(arr2[MaxIndex])
	arr2.pop(MaxIndex)
	if len(arr2) == 0:
		break
	Max = int(arr2[0][0])
	MaxIndex = 0
print(endString)