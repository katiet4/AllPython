from flask import request,Flask,render_template,session
app = Flask(__name__)
app.secret_key = 'HelloFriendFuckSociety'
@app.route('/users/<user>')
def ident(user:str):
	session['user'] = user
	return render_template('index.html',user="None")
@app.route('/usersget')
def get():
	return render_template('index.html',user=session['user'])
if __name__ == '__main__':
	app.run(debug = True)


