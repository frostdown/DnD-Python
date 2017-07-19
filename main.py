#!/usr/bin/python

import sys
import os
import json

class Character:
    #'Player character class'

    def __init__(self, name,  hitPoints, armorClass, initiative, spd, dex, const, intel, wis, char):
        self.hitPoints = hitPoints
        self.temporaryHitPoints = hitPoints
        self.armorClass = armorClass
        self.initiative = initiative
        self.speed = spd
        self.dexterity = dex
        self.constitution = const
        self.intelligence = intel
        self.wisdom = wis
        self.charisma = char
        self.name = name

class Spell:

    def __init__(self, spellName, spellType, castingTime, range, components, duration, description):
        self.spellName = spellName
        self.spellType = spellType
        self.castingTime = castingTime
        self.range = range
        self.components = components
        self.duration = duration
        self.description = description

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


#spells never change, I should be using tuple
spelldict = {}
#character needs to me mutable
characterdict = {}

#change the while loop to something meaningfull
while True:
    option = input('Select option\n' 
                   '1. Load File\n' 
                   '2. New Character\n'
                   '3. New Spell\n'
                   '4. Exit\n'
                   ': ')
    if option == '1':
        with open('DnDSave.json', 'r') as fp:
            spelldict = json.load(fp)
            characterdict = json.load(fp)

        print("not fully implemented")
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

with open('DnDSave.json', 'w') as fp:
    json.dump(spelldict, fp)
    json.dump(characterdict, fp)