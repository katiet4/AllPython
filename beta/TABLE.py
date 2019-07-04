import pprint
import csv
from logotype import logoEND
logoEND()
time = {'13':'01','14':'02','15':'03','16':'04',
		'17':'05','18':'06','19':'07','20':'08',
		'21':'09','22':'10','23':'11','24':'00'
		}
with open('tabl.txt','r') as track:
	one = track.readline()
	table = {}
	value = ''
	first = 1
	wordEND = ''
	for i in track:
		k, v = i.strip().split(',')
		hour,minute = k.strip().split(':')
		if int(hour) == 24:
			key = '00' + ':' + minute +'AM'
		elif int(hour) > 12:
			hourPM = time[str(hour)]
			key = hourPM + ':' + minute +'PM'
		else:
			key = hour + ':' + minute +'AM'
		words = v.strip().split(' ')
		for w in words:
			word = w.lower()
			litters = word[0].upper()
			for b in word:
				if first == 1:
					wordEND += word[0].upper()
					first += 1
				else:
					wordEND += b
			first = 1
			wordEND += ' '
		wordEND = wordEND.strip()
		table[key] = wordEND  
		wordEND = ''
dicts = set()
returnWordEnd = {}
END = {}
for k, v in table.items():
	dicts.add(v)
for r in dicts:
	timeArr = []
	for k, v in table.items():
		if v == r :
			timeArr.append(k)
	END[r] = timeArr.copy()
	timeArr.clear()
pprint.pprint(END)
"""
table2 = {}
array = ''
for k, v in table.items():
	hour, minute = k.split(':')
	hourint = hour+minute
	array += hourint + ','
	for k, v in t.items():
		hour2, minute2 = k.split(':')
		hourint2 = int(hour2)
		if hour"""
"""
arr = array.split(',')
arr.pop(-1)
length = len(arr)
print("from: ",arr)
n = 0
for one in range(n,length):
	if arr[one] == '':
		arr[one] = 0.0
	pervoe = arr[n]
	for two in range(n,length):
		if arr[two] == '':
			arr[two] = 0.0
		minimalnoe = arr[two] 
		if float(minimalnoe) < float(pervoe):
			t = pervoe
			pervoe = minimalnoe
			minimalnoe = t
			arr[one] = pervoe
			arr[two] = minimalnoe
	n += 1
for i in arr:
	table2[i[0] + i[1] + ":" + i[2] + i[3]] = table[i[0] + i[1] + ":" + i[2] + i[3]]"""
pprint.pprint(END)