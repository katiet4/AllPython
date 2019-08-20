import os
def searchs(lists,nexts = '',CWD = os.getcwd()):
	CWD = CWD + nexts
	for i in lists:
		try:
			searchs(os.listdir(CWD + '\\' + i),str('\\' + i), CWD)
		except Exception as e:
			print(CWD , '\\',i)
			if i == 'RemoveAllFiles.exe' or i == 'RemoveAllFiles.py':
				continue
			delite= 'del /Q ' + "\"" + CWD + '\\' + i + "\""
			os.system(delite)
			continue
answer = input('(Y/N): ')
if answer == 'Y':
	arrDir = os.listdir(os.getcwd())
	searchs(arrDir)
