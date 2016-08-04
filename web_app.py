from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Person

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')



@app.route('/ABOUT-US')
def AboutUs():
	return render_template('AboutUs.html')

@app.route('/MyProfile')
def MyProfile():
	return render_template('MyProfile.html')

@app.route('/SignIn')
def SignIn():
	if request.method == 'POST':
		pass
	#sername = request.form['username']
	return redirect(url_for('index'))

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUser():
	if (request.method == 'POST'):
		
		username= request.form['username']
		password= request.form['password']
		gender= request.form['gender']
		hometown= request.form['hometown']
		user= Person( username=username, gender = gender, hometown=hometown, password=password)
		session.add(user)
		session.commit()
		return render_template('main_page.html')
	else:
		return render_template('add_user.html')



@app.route('/France')
def test():
	return render_template('france.html')

@app.route('/India')
def test2():
	return render_template('india.html')

@app.route('/Peru')
def test3():
	return render_template('peru.html')


if __name__ == '__main__':
	app.run(debug=True)
