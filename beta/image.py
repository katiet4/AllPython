with open('hell.bmp','rb') as read:
	n = 0
	for i in read:
		string = str(i)
		reading = string.split('\\')
		print(reading[0])
		n+=1
print(n)