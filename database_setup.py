from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class Person(Base): 
	__tablename__ = 'person' 
	id = Column(Integer, primary_key=True) 
	name = Column(String)  
	username = Column(String)
	password = Column(String) 
	gender = Column(String)  
	hometown = Column(String)
	posts = relationship("Posts", uselist=True)

class Posts(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)   
	post = Column(String)
	country = Column(String) 
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship("Person")