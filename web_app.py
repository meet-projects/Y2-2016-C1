from flask import Flask, render_template, request, redirect, url_for, session
import ctypes
from ctypes import *
app = Flask(__name__)
app.secret_key = 'hi ted'
# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()


#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')



@app.route('/ABOUT-US')
def AboutUs():
	return render_template('AboutUs.html')

@app.route('/MyProfile')
def MyProfile():
	user = dbsession.query(Person).filter_by(id = session['user_id']).first()
	return render_template('MyProfile.html', user = user)

@app.route('/logout')
def logout():
	session.pop('user_id', None)
	return redirect(url_for('main'))

@app.route('/CreatePost', methods=['POST'])
def CreatePost():
	person_id = -1
	country = request.form['country']
	title = request.form['title']
	subject = request.form['subject']
	text = request.form['text']
	post = Posts(country=country, title=title, subject=subject, text=text, person_id=person_id)
	dbsession.add(post)
	dbsession.commit()
	return redirect(url_for('MyProfile'))

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
	if (request.method == 'POST'):
		username = request.form['username']
		password = request.form['password']
		user = dbsession.query(Person).filter_by(username = username).first()
		if user == None or user.password != password:
			return render_template('sign_in.html', error = True)
		else:
			session['user_id'] = user.id
			return render_template('main_page.html')
	else :
		return render_template('sign_in.html')
		

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUser():
	if (request.method == 'GET'):
		return render_template('add_user.html')
	else:
		name= request.form['name']
		username= request.form['username']
		password= request.form['password']
		gender= request.form['gender']
		hometown= request.form['hometown']
		user= Person(name=name, username=username, gender = gender, hometown=hometown, password=password)
		dbsession.add(user)
		dbsession.commit()
		return redirect(url_for('main'))



@app.route('/France')
def test():
	return render_template('france.html')

@app.route('/India')
def test2():
	return render_template('india.html')

@app.route('/Peru')
def test3():
	return render_template('peru.html')

@app.route('/country', methods=['POST'])
def country():
	post= request.form['post']
	country= request.form ['country']
	


	print(request.form)
	return '1'


@app.route('/addpost', methods=['POST'])
def subject():
	
	print(request.form)
	return '1'

if __name__ == '__main__':
	app.run(debug=True)
