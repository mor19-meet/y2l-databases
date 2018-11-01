from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(size, types, color, price):
	product object = Product(
		size = size,
		types = types,
		color = color,
		price = price)
	session.add(create_product)
	session.commit()

create_product(15, "hp", "black", 3000 )
create_product(14 , "apple" , "silver", 4000)

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  pass

def get_product(id):
  pass
