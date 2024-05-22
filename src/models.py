import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(Date, nullable=False)  # Corrected typo and data type



class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    # El nombre de esta persona.
    name = Column(String(250), nullable=False)
    # El género de esta persona.
    gender = Column(String(250))
    # El color de ojos de esta persona.
    eye_color = Column(String(250))
    # El color de pelo de esta persona.
    hair_color = Column(String(250))
    # La altura de la persona en centímetros.
    height = Column(Integer)
    # La masa de la persona en kilogramos.
    mass = Column(Integer)
    # El color de piel de esta persona.
    skin_color = Column(String(250))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    # El nombre de este planeta.
    name = Column(String(250), nullable=False)
    # El clima de este planeta.
    climate = Column(String(250))
    # El terreno de este planeta.
    terrain = Column(String(250))
    # El número de días estándar que le toma a este planeta completar una única órbita de su estrella local.
    orbital_period = Column(Integer)
    # El diámetro de este planeta en kilómetros.
    diameter = Column(Integer)
    # Un número que indica la gravedad de este planeta
    gravity = Column(Integer)
    # El porcentaje de la superficie del planeta que es agua o masas de agua naturales.
    surface_water = Column(Integer)
    # El número de horas estándar que le toma a este planeta completar una sola rotación sobre su eje.
    rotation_period = Column(Integer)
    # La población promedio de seres sintientes que habitan este planeta.
    population = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    # El nombre de esta nave estelar
    name = Column(String(250), nullable=False)
    # El modelo oficial de esta nave estelar.
    model = Column(String(250))
    # La clase de esta nave espacial.
    starship_class = Column(String(250))
    # El fabricante de esta nave estelar.
    manufacturer = Column(String(250))
    # El costo de esta nueva nave espacial.
    cost_in_credits = Column(Integer)
    # La longitud de esta nave estelar en metros.
    length = Column(Integer)
    # La cantidad de personal necesario para ejecutar o pilotar esta nave estelar.
    crew = Column(Integer)
    # La cantidad de personas no esenciales que esta nave espacial puede transportar.
    passengers = Column(Integer)
    # La velocidad máxima de esta nave estelar en la atmósfera.
    max_atmosphering_speed = Column(Integer)
    # La clase del hiperimpulsor de esta nave estelar.
    hyperdrive_rating = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    # El nombre de este Vehiculo
    name = Column(String(250), nullable=False)
    # El modelo oficial de este Vehiculo.
    model = Column(String(250))
    # La clase de este Vehiculo.
    vehicle_class = Column(String(250))
    # El fabricante de este Vehiculo.
    manufacturer = Column(String(250))
    # El costo de este Vehiculo.
    cost_in_credits = Column(Integer)
    # La longitud de este Vehiculo en metros.
    length = Column(Integer)
    # La cantidad de personal necesario para ejecutar o pilotar este Vehiculo.
    crew = Column(Integer)
    # La cantidad de personas no esenciales que esta Vehiculo puede transportar.
    passengers = Column(Integer)
    # La velocidad máxima de este Vehiculo en la atmósfera.
    max_atmosphering_speed = Column(Integer)
  

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    # El nombre de esta especie.
    name = Column(String(250), nullable=False)
    # La clasificación de esta especie.
    classification = Column(String(250), nullable=False)
    # La altura promedio de esta especie en centímetros..
    average_height = Column(Integer)
    # La esperanza de vida promedio de esta especie en años.
    average_lifespan = Column(Integer)
    # Los colores de ojos comunes para esta especie.
    eye_colors = Column(String(250))
    # Los colores de cabello comunes para esta especie.
    hair_colors = Column(String(250))
    # los colores de piel comunes para esta especie, "ninguno" si esta especie no suele tener piel.
    skin_colors = Column(String(250))
    # el idioma comúnmente hablado por esta especie.
    language = Column(String(250))



class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    species_id = Column(Integer, ForeignKey('species.id'))

    user = relationship(User, backref='favorites')
    character = relationship(Character, backref='favorites')
    planet = relationship(Planet, backref='favorites')
    starships = relationship(Starships, backref='favorites')
    vehicles = relationship(Vehicles, backref='favorites')
    species = relationship(Species, backref='favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
