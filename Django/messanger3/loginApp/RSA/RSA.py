from random import randint

def only(num):
		arr = []
		for i in range(2,(num//2)+1):
			if (num%i)==0:
				arr.append(i)
		return arr
def E(F):
	delF = only(F)
	while True:
		boo = True
		e = randint(3,10000)
		if e % 2 == 1:
			delE = only(e)
			for i in delE:
				if i in delF:
					boo = False
					break
			if boo :
				return e



		


	return ranE
justN = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
num = randint(0,int(len(justN))-1)
p=justN[num]
q=justN[num+1]
n = p*q
FuncN = (p-1)*(q-1)
e = E(FuncN)
d = 0
while True:
	for k in range(1,1000):
		if (k*FuncN+1) % e == 0:
			d = int((k*FuncN+1) / e)
	if d != 0:
		break
	else:
		e = E(FuncN)
m = input("message: ")
lenght = len(m)
r = 0
print(e)
print(d)
print(n)
encrypt = '|' 
for i in m:
	mN=ord(i)+r
	print(ord(i)+r)
	c = pow(mN,e) % n 
	encrypt += str(c)+'|'
	r+=1

print(encrypt)
r = 0
decrypt = ''
encryptArr= encrypt.split('|')
for i in encryptArr:
	if i == '':
		continue
	decrypt += chr((pow(int(i),d)%n)-r)
	print((pow(int(i),d)%n)-r)
	r+=1
print(decrypt)