import os
def searchs(lists,find = '',nexts = '',CWD = os.getcwd()):
	CWD = CWD + nexts
	for i in lists:
		try:
			searchs(os.listdir(CWD + '\\' + i),find,str('\\'+i), CWD)
		except Exception as e:
			if find == '':
				pass
			elif find == i:
				print(CWD + '\\' + i)
			continue

search = input('Find: ')
arrDir = os.listdir(os.getcwd())
searchs(arrDir,search)
