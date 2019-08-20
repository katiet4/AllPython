from flask import Flask, render_template,request,session
from password import check
from datetime import datetime
import time
from database import dataBase
from login import Login
from auntification import Aunt
from registartion import Reg
apps = Flask(__name__)
apps.config['base'] = {'host':'127.0.0.1',
						'user':'root',
						'password':'root',
						'database':'web'}
apps.config['base2'] = {'host':'127.0.0.1',
						'user':'root',
						'password':'root',
						'database':'fsociety'}
apps.secret_key = 'HelloElliotAlderson'
@apps.route('/')
def form():
	session['bool'] = False
	return render_template('login.html')
@apps.route('/registrat')
def R():
		return render_template('registration.html')
@apps.route('/log',methods = ['POST','GET'])
def login():
	Email = str(request.form['Email'])
	password = str(request.form['password'])
	try:
		ses = Login(apps.config['base2'],Email,password)
	except Exception as e:
		print("Error:", e)
	if ses == '0000000000000000000000000000000000000000000':
		return render_template('Error.html')
	else:
		try:
			booling = Aunt(apps.config['base2'],ses,Email)
		except Exception as e:
			print("Error:", e)
		session['bool'] = booling 
		if session['bool'] == False: 
			return render_template('Error.html')
		else:
			return render_template('page_one.html')
@apps.route('/reg',methods = ['POST','GET'])
def registr():
	Email = str(request.form['Email'])
	password = str(request.form['password'])
	ReapetPassword = str(request.form['passwordReapet'])
	try:
		ses = Reg(apps.config['base2'],Email,password,ReapetPassword)
	except Exception as e:
		print("Error:", e)
	if ses == '0000000000000000000000000000000000000000000':
		return render_template('Error.html')
	else:
		try:
			booling = Aunt(apps.config['base2'],ses,Email)
		except Exception as e:
			print("Error:", e)
		session['bool'] = booling
		if session['bool'] == False:  
			return render_template('Error.html')
		else:
			return render_template('page_one.html')
def log(allStr,quantitly,size):
	if session['bool'] == True: 
		road = 'logs/' + 'size=' + size + ' quantitly=' + quantitly + '.txt'
		dates=str(datetime.today().day) +"|"+ str(datetime.today().month) + "|" + str(datetime.today().year)
		with open (road,'a') as logs:
			print(allStr,file=logs)
			print('\n',file=logs)
		with dataBase(apps.config['base']) as cursor:
			_SQL = """INSERT INTO 
							alllogsfiles (Form,Route_addr,User_agent,Date,Time) 
							VALUES (%s,%s,%s,%s,%s)"""
			cursor.execute(_SQL,(str(request.form),
									str(request.remote_addr),
									str(request.user_agent),
									dates,
									str(time.strftime('%H:%M:%S %A'))))
	else:
		return render_template('Error.html')

@apps.route('/res',methods=['POST','GET'])
def res_form() -> 'html':
	if session['bool'] == True:
		First_name = str(request.form['first_name'])
		Last_name = str(request.form['last_name'])
		birthdayD = str(request.form['birthdayD'])
		birthdayM = str(request.form['birthdayM'])
		birthdayY = str(request.form['birthdayY'])
		quantitly = str(request.form['quantitly'])
		numbers_answer = str(request.form['numbers_answer'])
		numbers = str(request.form['numbers'])
		size = str(request.form['size'])
		all_pass = check(First_name, Last_name, birthdayD, birthdayM, birthdayY,
							quantitly, numbers_answer, numbers, size)
		if all_pass == "ERROR":
			return render_template('page_two.html' , alls = "Please,go to back and check all", quantitly = "ERROR")
		else:	
			allStr ='\n'.join(all_pass)
			log(allStr,str(len(allStr)),size)
			return render_template('page_two.html' , alls = allStr, quantitly = str(len(all_pass)))
	else:
		return render_template('Error.html')
@apps.route('/logs')
def logs():
	if session['bool'] == True:
		with dataBase(apps.config['base']) as cursor:
			_SQL = 'SELECT * from alllogsfiles'
			cursor.execute(_SQL)
			logs = cursor.fetchall()
			return render_template('table.html',FRUDT=logs)# 'page_two.html',Logs = str(end)
	else:
		return render_template('Error.html')
if __name__ == "__main__":
	apps.run(debug = True)