from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base

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
    return render_template('sign_in.html')

@app.route('/AddUser')
def add_user():
    return render_template('add_user.html')



@app.route('/test')
def test():
    return render_template('france.html')

@app.route('/test2')
def test2():
    return render_template('india.html')

@app.route('/test3')
def test3():
    return render_template('peru.html')


if __name__ == '__main__':
    app.run(debug=True)
