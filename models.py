from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from models import *

Base = declarative_base()

# Write your classes here :
class Product(Base):
    __tablename__ = "computers"
    id = Column(Integer, primary_key= True)
    size = Column(Integer)
    types = Column(String)
    #color = Column(String)
    price = Column(Integer)

