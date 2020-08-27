#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'rainer'

## https://repl.it/

# Grundbegriffe der Programmierung

## Zahlen in Python
# Ausgabe von Zahlen
print(5)
print(6)

# Grundrechenarten
print(5 + 4)
print(5 - 4)
print(5 * 4)
print(5 / 4)

# Klammern
print((5 + 4) * 3)

# Floats
print(1.25 + 2)

## Variablen in Python
a = 5
a = 5 + 6
print(a)
print(a * a)

b = 5
print(b * b * b)

age = 21
age2 = 18
print((age + age2) / 2)

average_age = (age + age2) / 2
print(average_age)

## Strings in Python
print("Hallo Welt")

name = "Max"
print(name)

# Strings zusammenführen
print("Ich bin: " + "Max")
print("Ich bin: " + name + ". Und wer bist du?")
print(f"Ich bin: {name}. Und wer bist du?")


# print("Ich bin: " + 4)  # --> Fehlermeldung: TypeError: must be str, not int

print("Ich bin: " + "4")

age = 22
print("Ich bin: " + str(age))

## Quiz: Zahl oder String

## Listen

# schlecht
student1 = "Max"
student2 = "Monika"
student3 = "Erik"
student4 = "Franziska"

# besser
students = ["Max", "Monika", "Erik", "Franziska"]
marks = [4, 3, 2, 1]
print(students)

# Zugriff auf Liste
# Über den Index
print(students[0])
print(students[0] + " & " + students[3])

# Durchschnitt der Noten berechnen
# naja
print((marks[0] + marks[1] + marks[2] + marks[3]) / 4)

# besser
print(sum(marks) / len(marks))

# best
import statistics

print(statistics.mean(marks))

## Element hinzufügen
students.append("Moritz")
print(students)

# Länge einer Liste
print(len(students))

## Element entfernen
planets = ["Erde", "Mars", "Jupiter", "Saturn", "Pluto"]
planets.pop()  # letztes Element der Liste wird entfernt
print(planets)

p = planets.pop()
print(p)

students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
del students[3]
print(students)

students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
students.remove("Monika")
print(students)

## Daten umwandeln
# Integer -> String
a = str(42)

# String -> Integer
a = int("42")

# String -> Float
a = float("42")

## Dictionaries
d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print(d)

print(d["Helsinki"])

## Daten einem Dictionary hinzufügen
d.update({"Wien": "VIE"})

## Key in einem Dictionary löschen
# del (d["Budapest"])
print(d)

if "Budapest" in d:
    print("Budapest ist im Dictionary enthalten")
if "Saigon" in d:
    print("Saigon ist im Dicionary enthalten")

print(d["Saigon"])
print(d.get("Saigon"))

# print(d["Budapest"])  # --> KeyError: 'Budapest'

d = {"München": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}
for key in d:
    value = d[key]
    print(key)
    print(value)

for key, value in d.items():
    print(key + ": " + value)

## Kommentare - einzeilig
"""
mehrzeilige
"""

## IF / ELIF / ELSE
if 6 < 5:
    print("JA")

print(6 < 5)
print(5 < 6)

result = 5 < 6
if result:
    print("5 ist kleiner als 6")

## Vergleichsoperatoren
"""
== gleich
!= ungleich
< kleiner
<= kleiner gleich
> größer
>= größer gleich
"""

## Vergleichsoperatoren verknüpfen
# and
# or
a = 5
b = 6

if a > 1 and b < 10:
    print("a größer 1 und b kleiner 10")

if a != b or b > 2:
    print("a nicht b, oder b größer 2")

## in-Operator
students = ["Max", "Monika", "Erik", "Franziska"]
print("Monika" in students)
print("Moritz" in students)

if "Monika" in students:
    print("Ja, die Monika studiert hier!")
else:
    print("Nein, die Monika studiert hier nicht!")
if "Moritz" in students:
    print("Ja, der Moritz studiert hier!")
else:
    print("Nein, der Moritz studiert hier nicht!")


sentence = "Ja, die Monika studiert hier!"
if "!" in sentence:
    print("JA")
else:
    print("NEIN")
    
## not-Operator
# negiert eine Aussage
names = ["Rainer", "Barbara", "Alexander"]

to_find = "Emanuel"

if not to_find in names:
    print(f"{to_find} ist nicht in der Namesliste enthalten.")

## WHILE
counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

print("Hallo Welt")

## FOR
liste = ["Max", "Moritz", "Monika"]
for i in liste:
    print(i)

for i in range(0, 10):
    print(i)

## continue
for i in range(0, 10):
    if i == 3:
        continue
    print(i)

## break
for i in range(0, 10):
    if i == 3:
        break
    print(i)

## Funktionen
def multi_print(name, count):
    for i in range(0, count):
        print(name)

multi_print("Hallo!", 5)

## Dateien (mittels with-Context Manager)
## Datei einlesen

dateiname = "zitate.txt"

with open(dateiname, mode="r") as file:
    for line in file:
        print(line)

## Datei schreiben
studenten_datei = "students.txt"

with open(studenten_datei, mode="w") as file:
    for student in ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]:
        file.write(student)

## CSV-Datei lesen
import csv
csv_datei = "Vornamen.csv"
with open(csv_datei, mode="r") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        print(row)

with open(csv_datei, mode="r") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        print(row)


# Datum
from datetime import datetime

print(datetime.now())

# random
from random import randint, choice
print(randint(0, 100))

# os
import os
print(os.listdir())

# Userinput
log = input('Was ist dir heute wiederfahren?\n')

# Passwörter
from getpass import getpass

secret = getpass("Deine Frage an das Orakel")

print(log, secret)