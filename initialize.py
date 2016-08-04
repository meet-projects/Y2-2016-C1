from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person, Posts

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.
ron = Person(name='Ron', username = 'Ronmiles', password = 123456, gender = 'Male', hometown = 'jerusalem')
post1 = Posts(text = 'jerusalem is great', country = 'israel', person = ron)
post2 = Posts(text = 'jerusalem is great2', country = 'israel', person = ron)
session.add(ron)
session.add(post1)
session.add(post2)
session.commit()
print(ron.posts[0].text)
print(ron.posts[1].text)
