import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(50), nullable=False)
    email= Column(String(50),nullable=False)
    


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    height = Column(Integer, nullable=True)
    skin_color = Column(String(20), nullable=True)
    skills = Column(String(100), nullable=True)
    origin = Column(String(50), nullable=False)

 
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    color = Column(String(50), nullable=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    planet_type = Column(String(50), nullable=False)
    planet_size = Column(String(50), nullable=True)


class FavoritesCharact(Base):
    __tablename__ = 'Favorites characters'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    charactid = Column(Integer,ForeignKey('characters.id'))
    character = relationship(Characters)



class FavoritesPlanets(Base):
    __tablename__ = 'Favorites planets'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    planetid = Column(Integer,ForeignKey('planets.id'))
    planet = relationship(Characters)

class FavoritesVeh(Base):
    __tablename__= 'Favorites vehicles'
    id = Column(Integer, primary_key=True)
    vehid = Column(Integer,ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)






    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




# ANOTHER WAY TO DO IT 

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'user'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     userid = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     email= Column(String(50),nullable=False)

# class Characters(Base):
#     __tablename__ = 'characters'
#     charactid = Column(Integer, primary_key=True)
#     name = Column(String(50),nullable=False)
#     height = Column(Integer, nullable=True)
#     skin_color = Column(String(20), nullable=True)
#     skills = Column(String(100), nullable=True)
#     origin = Column(String(50), nullable=False)

 
# class Vehicles(Base):
#     __tablename__ = 'vehicles'
#     vehicid = Column(Integer, primary_key=True)
#     name = Column(String(50),nullable=False)
#     vehicle_type = Column(String(50), nullable=False)
#     color = Column(String(50), nullable=True)


# class Planets(Base):
#     __tablename__ = 'planets'
#     planetid = Column(Integer, primary_key=True)
#     name = Column(String(50),nullable=False)
#     planet_type = Column(String(50), nullable=False)
#     planet_size = Column(String(50), nullable=True)


# class Favorites(Base):
#     __tablename__ = 'favorites'
#     favid = Column(Integer, primary_key=True)
#     charactid = Column(Integer,ForeignKey('characters.charactid'))
#     planetid = Column(Integer,ForeignKey('planets.planetid'))
#     userid = Column(Integer,ForeignKey('user.userid'))
#     vehicid = Column(Integer,ForeignKey('vehicles.vehicid'))
#     characters = relationship(Characters)
#     planets = relationship(Planets)
#     user = relationship(User)
#     vehicles = relationship(Vehicles)

    


#     def to_dict(self):
#         return {}
# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')