from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
  picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'), ondelete='CASCADE')
    user= relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class Items(Base):
    __tablename__ = 'items'


    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'), ondelete='CASCADE')
    category = relationship(Category)
    user_id= Column(Integer, ForeignKey('user.id'), ondelete='CASCADE')
    user= relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'                  : self.id,
           'name'                : self.name,
           'description'         : self.description,
           'category'            : self.category.serialize,
       }



engine = create_engine('sqlite:///catalog.db')
 

Base.metadata.create_all(engine)