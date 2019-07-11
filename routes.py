from flask import Flask, render_template
from models import db, User
from forms import UsersForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)

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
			