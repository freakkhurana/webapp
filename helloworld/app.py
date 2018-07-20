from flask import Flask, render_template, redirect, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

#app config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'none'
app.config['MYSQL_PASSWORD'] = 'none'





@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		some_json = request.get_json()
		userdetails = request.form
		name = userdetails['name']
		email = userdetails['email']
		password = userdetails['password']
	    MySQLdb.connect('localhost', 'root','1234')
	    cur = mysql.connection.cursor()
	    cur.execute("INSERT INTO users(name,email) VALUES(%s, %s)",(name, email))
	    mysql.connection.commit()
	    cur.close()
	    return jsonify({ 'you sent': some_json ,}), 201
	else:
	    return render_template('index.html' )

@app.route('/multi/<name:userdetails['name']>', methods=[ 'GET' ])
def fetch(name):
	cur = mysql.connection.cursor()
	resultvalue= cur.execute("SELECT * FROM users")
	if resultvalue >0:
		userdetails = cur.fetchall{}
		return render_template('user.html', userdetails=userdetails)
	else:
		return jsonify({ 'message': you have to register first })

if __name__ == '__main__':
	app.run(debug=True)