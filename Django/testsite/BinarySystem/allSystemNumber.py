
from LogErrors.models import ErrorsLogs
import datetime
def main (which, Arifm, num1, num2):
		try:
			num1Arr = str(num1) 
			num2Arr = str(num2)
			
			num1Dec = 0
			num2Dec = 0

			letters = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,'a':10, 'b':11, 'v':12, 'd':13, 'e':14, 'f':15}

			s = 0
			for i in range(int(len(num1Arr))-1,-1,-1):
				if num1Arr[i] in letters:
					i = letters[num1Arr[i]]
					num1Dec += i * pow(which, s)
					s +=1
					continue
				num1Dec += int(num1Arr[i]) * pow(which, s)
				s +=1
			
			s = 0
			for i in range(int(len(num2Arr))-1,-1,-1):
				if num2Arr[i] in letters:
					i = letters[num2Arr[i]]
					num2Dec += i * pow(which, s)
					s +=1
					continue
				num2Dec += int(num2Arr[i]) * pow(which, s)
				s +=1
			print(str(num1Dec)+" "+str(num2Dec))
			num1Dec = int(num1Dec)
			num2Dec = int(num2Dec)
			if(Arifm == '+'):
				resultDec = num1Dec + num2Dec
			elif(Arifm == '-'):
				resultDec = num1Dec - num2Dec
			elif(Arifm == '/'):
				resultDec = num1Dec / num2Dec
			else:
				resultDec = num1Dec * num2Dec

			resultBi = bin(round(resultDec))[2:]
			resultOct = oct(round(resultDec))[2:]
			resultHex = hex(round(resultDec))[2:]
			num1Bi = bin(num1Dec)[2:]
			num2Bi = bin(num2Dec)[2:]
			num1Oct = oct(num1Dec)[2:]
			num2Oct = oct(num2Dec)[2:]
			num1Hex = hex(num1Dec)[2:]
			num2Hex = hex(num2Dec)[2:]
			return {'dec': [num1Dec, num2Dec, resultDec],
					'bin': [num1Bi, num2Bi, resultBi],
					'oct': [num1Oct, num2Oct, resultOct],
					'hex': [num1Hex, num2Hex, resultHex]}
		except Exception as e:
			d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
			d.save()
