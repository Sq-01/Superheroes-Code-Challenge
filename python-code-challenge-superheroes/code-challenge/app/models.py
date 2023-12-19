from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    powers = db.relationship('HeroPower', back_populates='hero')
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String)



class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    heroes = db.relationship('HeroPower', back_populates='power')
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(20))



class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(Enum('Strong', 'Weak', 'Average', name='strength_types'))    
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))


    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heroes')
