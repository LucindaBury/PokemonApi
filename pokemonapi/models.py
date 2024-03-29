from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)


class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    classification = Column(String(150))
    type1 = Column(String(50))
    type2 = Column(String(50))
    generation = Column(Integer)
    # One to one relationship with PokemonStats, uselist = False means that there will be only one PokemonStats object for each Pokemon object
    stats = relationship("PokemonStats", backref="pokemon", uselist=False)


class PokemonStats(Base):
    __tablename__ = "pokemon_stats"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    height_m = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)
    attack = Column(Integer, nullable=True)
    
    #When defining a float column in a database table, you can specify the precision and scale. The precision determines the total number of digits that can be stored, while the scale determines the number of digits to the right of the decimal point. For example, a float(6,2) column can store a number with up to 6 digits, and 2 digits to the right of the decimal point.
    