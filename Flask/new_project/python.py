from random import randint
def size1(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size2(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size3(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size4(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size5(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size6(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size7(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size8(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size9(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > (int(quantitly) * int(quantitly)):
			break
def size10(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def size11(all_passwd,elem,quantitly,error,big_quantitly):
	while len(all_passwd) < int(quantitly):
		all_passwd.add(elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))]+
						elem[randint(0,(len(elem)-1))])
		error+=1
		if error > big_quantitly:
			break
def passwd(first_name:str="false", last_name:str="false", birthdayD:str="false",
			birthdayM:str="false", birthdayY:str="false",quantitly:str="0" ,
			numbers_answer:str="no", numbers:str = "1,2,3,4,5,6,7,8,9,0",
			size:str="1"):
	if(numbers == "" or numbers == " "):
		numbers = "1,2,3,4,5,6,7,8,9,0"
	if(quantitly == "" or quantitly == " "):
		quantitly = "0"
	if(size == "" or size == " "):
		size = "1"
	numbers_list = numbers.split(',')
	all_passwd = set()
	resultat = 0
	elem = []
	if(first_name == "false" or first_name == "" or first_name == " "):
		resultat+=1
	else:
		elem.append(first_name)
		elem.append(first_name.upper())
		elem.append(first_name.lower())
	if(last_name == "false" or last_name == "" or last_name == " "):
		resultat+=1
	else:
		elem.append(last_name)
		elem.append(last_name.upper())
		elem.append(last_name.lower())
	if(birthdayD == "false" or birthdayD == "" or birthdayD == " "):
		resultat+=1
	else:
		elem.append(birthdayD)
	if(birthdayM == "false" or birthdayM == "" or birthdayM == " "):
		resultat+=1
	else:
		elem.append(birthdayM)
	if(birthdayY == "false" or birthdayY == "" or birthdayY == " "):
		resultat+=1
	else:
		elem.append(birthdayY)
	if ((numbers_answer.upper()) == "YES" or numbers_answer == "" or numbers_answer == " "):
		for i in numbers_list:
			elem.append(i)
	error = 0
	big_quantitly=(int(quantitly) * 10)
	if size == "1":
		size1(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "2":
		size2(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "3":
		size3(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "4":
		size4(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "5":
		size5(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "6":
		size6(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "7":
		size7(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "8":
		size8(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "9":
		size9(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "10":
		size10(all_passwd, elem, quantitly,error,big_quantitly)
	elif size == "11":
		size11(all_passwd, elem, quantitly,error,big_quantitly)
	else:
		return all_passwd
	return all_passwd

