w = open("HALionOne.dll",'wb')
binary = {}
i = 0
while i < 1000:
	w.write(b'x01111')
	i+=1
w.close()