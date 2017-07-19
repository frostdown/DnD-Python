#!/usr/bin/python

import sys
import os
import sqlite3
import sqlalchemy

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


conn = sqlite3.connect('DnD.db')

Base = declarative_base()

class Character(Base):
    'Player character class'
    __table__ = 'Character'
    hitPoints = Column(Integer, primary_key=True)
    temporaryHitPoints = Column(String(250), nullable=False)
    armorClass = Column(Integer, primary_key=True)
    initiative = Column(Integer, primary_key=True)
    speed = Column(Integer, primary_key=True)
    strength = Column(Integer, primary_key=True)
    strengthMod = Column(Integer, primary_key=True)
    dexterity = Column(Integer, primary_key=True)
    dexterityMod = Column(Integer, primary_key=True)
    constitution = Column(Integer, primary_key=True)
    constitutionMod = Column(Integer, primary_key=True)
    intelligence = Column(Integer, primary_key=True)
    intelligenceMod = Column(Integer, primary_key=True)
    wisdom = Column(Integer, primary_key=True)
    wisdomMod = Column(Integer, primary_key=True)
    charisma = Column(Integer, primary_key=True)
    charismaMod = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

  #  def __init__(self, name,  hitPoints, armorClass, initiative, spd, dex, const, intel, wis, char):
  #      self.hitPoints = hitPoints
  #      self.temporaryHitPoints = hitPoints
  #      self.armorClass = armorClass
  #      self.initiative = initiative
  #      self.speed = spd
  #      self.dexterity = dex
  #      self.constitution = const
  #      self.intelligence = intel
  #      self.wisdom = wis
  #      self.charisma = char
  #      self.name = name

class Spell(Base):

    __table__ = 'Spells'
    self = Column(String(250), nullable=False)
    spellName = Column(String(250), nullable=False)
    spellType = Column(String(250), nullable=False)
    castingTime = Column(String(250), nullable=False)
    range = Column(String(250), nullable=False)
    components = Column(String(250), nullable=False)
    duration = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

#    def __init__(self, spellName, spellType, castingTime, range, components, duration, description):
#        self.spellName = spellName
#        self.spellType = spellType
#        self.castingTime = castingTime
#        self.range = range
#        self.components = components
#        self.duration = duration
#        self.description = description

def newSpell():
    spellName = input('Spell Name: ')
    spellType = input('Spell Type: ')
    castingTime = input('Casting Time: ')
    range = input('Range: ')
    components = input('Components: ')
    duration = input('Duration: ')
    description = input('Description: ')

    spell = Spell(spellName, spellType, castingTime, range, components, duration, description)
    return spell

def newCharacter():
    name = input('Name: ')
    hitPoints = input('Hit Points: ')
    armorClass = input('Armor Class: ')
    initiative = input('Initiative: ')
    spd = input('Speed: ')
    dex = input('Dexterity:')
    const = input(' Constitution: ')
    intel = input('Intelligence: ')
    wis = input('Wisdom: ')
    char = input('Charisma: ')

    character = Character(name, hitPoints, armorClass, initiative, spd, dex, const, intel, wis, char)
    return character

spelldict = {}
characterdict = {}

#change the while loop to something meaningfull
while True:
    option = input('Select option\n' 
                   '1. Load Character\n' 
                   '2. New Character\n'
                   '3. New Spell\n'
                   '4. Exit\n'
                   ': ')
    if option == '1':
        print("not implemented")
    elif option == '2':
        character = newCharacter()
        name = character.name
        if name in characterdict:
            print('Error character name already used\n')
        else:
            characterdict[name] = character

    elif option == '3':
        spell = newSpell()
        name = spell.spellName
        if name in spelldict:
            print('Error spell already exists\n')
        else:
            spelldict[spell.spellName] = spell
    elif option == '4':
        break

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)


conn.commit()
conn.close()