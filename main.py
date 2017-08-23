#!/usr/bin/python
import sys
import os
import pickle

class Character:
    #'Player character class'

    def __init__(self, name,  hitPoints, armorClass, initiative, spd, str,  dex, const, intel, wis, char, level):
        self.hitPoints = hitPoints
        self.temporaryHitPoints = hitPoints
        self.armorClass = armorClass
        self.initiative = initiative
        self.speed = spd
        self.strength = str
        self.dexterity = dex
        self.constitution = const
        self.intelligence = intel
        self.wisdom = wis
        self.charisma = char
        self.name = name
        self.level = level
        self.experience = 0
        self.equipment = []
        self.spells = []
        self.skills = []

    def add_xp(self, xp):
        self.experience += xp
    def add_spell_to_list(self, spell):
        self.spells.append(spell)

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
    spellName = input('Spell Name:')
    spellType = input('Spell Type:')
    castingTime = input('Casting Time:')
    range = input('Range:')
    components = input('Components:')
    duration = input('Duration:')
    description = input('Description:')

    spell = Spell(spellName, spellType, castingTime, range, components, duration, description)
    return spell

def newCharacter():
    name = input('Name:')
    hitPoints = input('Hit Points:')
    armorClass = input('Armor Class:')
    initiative = input('Initiative:')
    spd = input('Speed:')
    str = input('Strength:')
    dex = input('Dexterity:')
    const = input('Constitution:')
    intel = input('Intelligence:')
    wis = input('Wisdom:')
    char = input('Charisma:')
    level = input('Level:')

    character = Character(name, hitPoints, armorClass, initiative, spd, str, dex, const, intel, wis, char, level)
    return character

def playCharacter(player, spelldict):
    while True:

        option = input('1.Show available spells\n2.Show prepared spells\n3.Add to spell list\n:')
        if option == '1':
            for x in player.spells:
                print(x.spellName, ':')
                print('Casting time:', x.castingTime)
                print('Range:', x.range)
                print('Duration:', x.duration)
                print(x.description, '\n')
        elif option == '2':
            #del player.spells[:]
            break
        elif option == '3':
            for x in spelldict:
                print(x)
            newspellname = input('Spell name:')
            newspell = spelldict[newspellname]
            player.add_spell_to_list(newspell)
    return player

with open('DnDSave.p', 'rb') as fp:
    spelldict = pickle.load(fp)
with open('DnDcharSave.p', 'rb') as pp:
    characterdict = pickle.load(pp)

#characterdict = {}

#change the while loop to something meaningfull
while True:
    option = input('Select option\n' 
                   '1. Load Character\n' 
                   '2. New Character\n'
                   '3. New Spell\n'
                   '4. Exit\n'
                   ': ')
    if option == '1':
        for x in characterdict:
            print(x)
        name = input('Character Name:')
        currentCharacter = characterdict[name]

        currentCharacter = playCharacter(currentCharacter, spelldict)
        characterdict.pop(name)
        characterdict[name] = currentCharacter

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

with open('DnDSave.p', 'wb') as fp:
    pickle.dump(spelldict, fp)
with open('DnDcharSave.p', 'wb') as pp:
    pickle.dump(characterdict, pp)