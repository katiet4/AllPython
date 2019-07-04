import pprint,csv,datetime
from logotype import logoEND
logoEND()
def convert(time:str):
	return datetime.datetime.strptime(time,'%H:%M').strftime('%I:%M%p')
with open('tabl.txt','r') as track:
	one = track.readline()
	table = {}
	value = ''
	for i in track:
		k, v = i.strip().split(',')
		v = v.title()
		table[convert(k)] = v
		
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