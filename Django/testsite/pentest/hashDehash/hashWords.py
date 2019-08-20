from LogErrors.models import ErrorsLogs
import datetime
def lete():

	return {"0" : "0","1" : "1","2" : "2","3" : "3","4" : "4","5" : "5","6" : "6","7" : "7","8" : "8","9" : "9",
	" " : "10","!" : "11","\"" : "12","#" : "13","$" : "14","%" : "15","&" : "16","'" : "17","(" : "18",")" : "19",
	"*" : "20","+" : "21","," : "22","-" : "23","." : "24","/" : "25",":" : "26",";" : "27","<" : "28","=" : "29",
	">" : "30","?" : "31","@" : "32","A" : "33","B" : "34","C" : "35","D" : "36","E" : "37","F" : "38","G" : "39",
	"H" : "40","I" : "41","J" : "42","K" : "43","L" : "44","M" : "45","N" : "46","O" : "47","P" : "48","Q" : "49",
	"R" : "50","S" : "51","T" : "52","U" : "53","V" : "54","W" : "55","X" : "56","Y" : "57","Z" : "58","[" : "59",
	"\\" : "60","]" : "61","^" : "62","_" : "63","`" : "64","a" : "65","b" : "66","c" : "67","d" : "68","e" : "69",
	"f" : "70","g" : "71","h" : "72","i" : "73","j" : "74","k" : "75","l" : "76","m" : "77","n" : "78","o" : "79",
	"p" : "80","q" : "81","r" : "82","s" : "83","t" : "84","u" : "85","v" : "86","w" : "87","x" : "88","y" : "89",
	"z" : "90","{" : "91","|" : "92","}" : "93","~" : "94","Г" : "95","Д" : "96","Е" : "97","Ё" : "98","Ж" : "99",
	"З" : "100","И" : "101","Й" : "102","К" : "103","Л" : "104","М" : "105","Н" : "106","О" : "107","П" : "108",
	"Р" : "109","С" : "110","Т" : "111","У" : "112","Ф" : "113","Х" : "114","Ц" : "115","Ч" : "116","Ш" : "117",
	"Щ" : "118","Ъ" : "119","Ы" : "120","Ь" : "121","Э" : "122","Ю" : "123","Я" : "124","а" : "125","б" : "126",
	"в" : "127","г" : "128","д" : "129","е" : "130","ё" : "131","ж" : "132","з" : "133","и" : "134","й" : "135",
	"к" : "136","л" : "137","м" : "138","н" : "139","о" : "140","п" : "141","р" : "142","с" : "143","т" : "144",
	"у" : "145","ф" : "146","х" : "147","ц" : "148","ч" : "149","ш" : "150","щ" : "151","ъ" : "152","ы" : "153",
	"ь" : "154","А" : "155","Б" : "156","В" : "157" ,"э" : "159","ю" : "160","я" : "161","џ" : "162","‰" : "163",
	"љ" : "164","Ђ" : "165","€" : "166","‹" : "167",'\r':'168','\n':"169"}
def hash(key = 0, text = ''):
	try:
		key = int(key)
		letters = lete()
		endText = ''
		where = 0
		newLetters = {}
		allArrs = []
		for i in range(0,500):
			allArrs.append([])
		for i in range(0,int(len(allArrs))):
			for r in letters:
				allArrs[i].append(key)
				key +=1 
		for i in letters:
			newLetters[i] = []
			for r in allArrs:
				newLetters[i].append(r[where])
			where+=1
		where = 0
		for i in text:
			endText += str(hex(newLetters[i][where])[2:])+'|'
			where+=1
		return endText
	except Exception as e:
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
		return e
def De_hash(key, text):
	try:
		key = int(key)
		letters = lete()
		endText = ''
		where = 0
		newLetters = {}
		allArrs = []
		for i in range(0,500):
			allArrs.append([])
		for i in range(0,int(len(allArrs))):
			for r in letters:
				allArrs[i].append(key)
				key +=1 
		for i in letters:
			newLetters[i] = []
			for r in allArrs:
				newLetters[i].append(r[where])
			where+=1
		where = 0
		s = 0
		textArr = text.split('|') 
		num2Dec = 0
		letters2 = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
		which = 16
		for num2Arr in textArr:
			for i in range(int(len(num2Arr))-1,-1,-1):
				if num2Arr[i] in letters2:
					i = letters2[num2Arr[i]]
					num2Dec += i * pow(which, s)
					s +=1
					continue
				
				num2Dec += int(num2Arr[i]) * pow(which, s)
				s +=1
			for i in letters:
				if num2Dec in newLetters[i]:
					endText += i
			s = 0
			num2Dec = 0
		return endText
	except Exception as e:
		d = ErrorsLogs(Date = str(datetime.datetime.today().day)+'.'+str(datetime.datetime.today().month)+'.'+str(datetime.datetime.today().year),
							Link = 'hashDehash',
							Error = e)
		d.save()
		return e
