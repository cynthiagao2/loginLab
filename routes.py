from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from forms import UsersForm
from flask_heroku import Heroku

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Leland2020@localhost/usersdb'
heroku = Heroku(app)
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():

	form = UsersForm()
	if request.method == 'GET':
		return render_template('add_user.html', form=form)
	else:
		if form.validate_on_submit():
			first_name = request.form['first_name']
			age = request.form['age']
			new_user = User(first_name=first_name, age=age)
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('index'))

@app.route('/read', methods=['GET'])
def read():
	names = User.query.all()
	return render_template('read.html', names=names)

@app.route('/delete', methods=['GET', 'POST'])
def delete():

	form = UsersForm()
	if request.method == 'GET':
		return render_template('delete.html', form=form)
	else:
		if form.validate_on_submit():
			user_id = request.form['user_id']
			db.session.delete()
			db.session.commit()
			return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(debug=True)