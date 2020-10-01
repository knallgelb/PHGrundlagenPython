#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'rainer'

"""
Hangman
"""


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

iterator = iter(HANGMANPICS)

from getpass import getpass

geheimnis = getpass("dein Geheimnis\n")
charaters_found = []

def print_guess(geheimnis, values):
    return "_".join(x for x in geheimnis if x in values)

while True:
    guess_char = input("Dein Vorschlag?\n")
    if guess_char not in geheimnis:
        try:
            print(next(iterator))
        except StopIteration:
            print("Game Over")
            break
    else:
        charaters_found.append(guess_char)
        if len(set(charaters_found)) == len(set(geheimnis)):
            print("Gewonnen :)")
            break
    print(print_guess(geheimnis, charaters_found))
