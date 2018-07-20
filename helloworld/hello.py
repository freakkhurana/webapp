from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import Registration, Login


app = Flask(__name__)
app.config['SECRET_KEY'] = '2f6532eddd1a09df473d103fa7025941'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


posts=[
{
	"author": "vipin khurana",
	"title": "on the name of fifa",
	"date": "18.01.2017",
	"content": "hii thie ie based on my project",

},

{
	"author": "bunny khurana",
	"title": "on the name of fifa world cup",
	"date": "22.01.2017",
	"content": "hii thie ie based on my project",

}

]


@app.route("/")
def home():
	return render_template('home.html',posts=posts)


@app.route("/about")
def about():
	return render_template('about.html',title='about')

@app.route("/register", methods=['GET','POST'])
def register():
	form = Registration()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}', 'success')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('you have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('login is not succesful. check username and password','danger')
			

	return render_template('login.html',title='Login', form=form)		

if __name__ == "__main__":
	app.run(debug=True)
			