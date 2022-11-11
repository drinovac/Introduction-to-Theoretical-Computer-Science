from re import X
import sys

from numpy import append

def epsilon(stanje, lista_prijelaza) :
    for line in lista_prijelaza:
        if(line[0][0] == stanje and line[0][1] == '$'):
            for i in line[1]:
                if(i not in trenutna_stanja):
                    trenutna_stanja.append(i)
                    epsilon(i, lista_prijelaza)

def epsilon1(stanje, lista_prijelaza) :
    for line in lista_prijelaza:
        if(line[0][0] == stanje and line[0][1] == '$'):
            for i in line[1]:
                if(i not in nova_lista and i != '#'):
                    nova_lista.append(i)
                    epsilon1(i, lista_prijelaza)


polje = []
i = 0
for line in sys.stdin:
    polje.insert(i, line)
    i = i + 1


ulazi = polje[0].strip()
stanja = polje[1].strip()
simboli = polje[2].strip()
prih_stanje = polje[3].strip()
poc_stanje = polje[4].strip()
prijelazi = polje[5:]

ulazi = ulazi.split('|')
stanja = stanja.split(',')
simboli = simboli.split(',')

ulazna_lista = []

for line in ulazi:
    line = line.split(',')
    ulazna_lista.append(line)

lista_prijelaza = []

for line in prijelazi:
    line = line.strip()
    line = line.split('->')
    unutarnja_lista = []
    poc_ul = line[0].split(',')
    poc_iz = line[1].split(',')
    unutarnja_lista.append(poc_ul)
    unutarnja_lista.append(poc_iz)
    lista_prijelaza.append(unutarnja_lista)


"""provjera ima li pocetno stanje $ prijelaze"""
trenutna_stanja = []
trenutna_stanja.append(poc_stanje)
""" 
for line in lista_prijelaza:
    if(line[0][0] == poc_stanje and line[0][1] == '$'):
        for i in line[1]:
            trenutna_stanja.append(i) """
epsilon(poc_stanje,lista_prijelaza)

trenutna_stanja.sort()
poc_kopija = trenutna_stanja

"""iteracija kroz listu ulaznih nizova gdje provjeravam
ima li prijelaza iz trenutnih stanja u nova stanja"""

for line in ulazna_lista:
    trenutna_stanja = poc_kopija
    print(*poc_kopija, sep=",", end="")
    for line_char in line:
        nova_lista = []
        for stanje in trenutna_stanja:
            for prijelaz in lista_prijelaza:
                if(prijelaz[0][0] == stanje and prijelaz[0][1] == line_char):
                    for j in prijelaz[1]:
                        if(j not in nova_lista and j != '#'):
                            nova_lista.append(j)
                            epsilon1(j, lista_prijelaza)
          
        if(len(nova_lista) == 0):
            nova_lista.append('#')
                
        nova_lista.sort()
        print("|", end="")
        print(*nova_lista,sep=",",end="")
        trenutna_stanja = nova_lista
    print()
             