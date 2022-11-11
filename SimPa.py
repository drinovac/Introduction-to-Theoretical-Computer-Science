from pickle import TRUE
from re import X
import sys

from numpy import append

polje = []
i = 0
for line in sys.stdin:
    polje.insert(i, line)
    i = i + 1


ulazi = polje[0].strip()
stanja = polje[1].strip()
ulazni_znakovi = polje[2].strip()
znakovi_stoga = polje[3].strip()
prihvatljiva_stanja = polje[4].strip()
poc_stanje = polje[5].strip()
poc_znak_stoga = polje[6].strip()
prijelazi = polje[7:]

ulazi_lista = ulazi.split('|')
lista_ulaza = []

for ulaz in ulazi_lista:
    lista_ulaza.append(ulaz.split(','))

stanja = stanja.split(',')
ulazni_znakovi = ulazni_znakovi.split(',')
znakovi_stoga = znakovi_stoga.split(',')
prihvatljiva_stanja = prihvatljiva_stanja.split(',')

lista_prijelaza = []

for line in prijelazi:
    line = line.strip()
    line = line.split('->')
    lista_linije = []
    lijeva_lista = line[0].split(',')
    desna_lista = line[1].split(',')

    lista_linije.append(lijeva_lista)
    lista_linije.append(desna_lista)

    lista_prijelaza.append(lista_linije)



for ulaz in lista_ulaza:
    print(poc_stanje,"#",poc_znak_stoga, sep='', end="|")

    trenutno_stanje = poc_stanje
    stog = poc_znak_stoga
    

    for znak in ulaz:
        flag = False
        for prijelaz in lista_prijelaza:
            if(prijelaz[0][0] == trenutno_stanje and prijelaz[0][1] == '$' and prijelaz[0][2] == stog[0]):
                trenutno_stanje = prijelaz[1][0]
                stog = stog[1:len(stog)]
                if(prijelaz[1][1] == '$'):
                    stog = '$'
                else:
                    stog = prijelaz[1][1] + stog 
                print(trenutno_stanje,"#",stog,sep='',end="|")
                
        for prijelaz in lista_prijelaza:
            if(prijelaz[0][0] == trenutno_stanje and prijelaz[0][1] == znak and prijelaz[0][2] == stog[0]):
                flag = True
                trenutno_stanje = prijelaz[1][0]
                stog = stog[1:len(stog)]
                if(prijelaz[1][1] != '$'):
                    stog = prijelaz[1][1] + stog                
                print(trenutno_stanje,"#",stog,sep='',end="|")
                break
        
            

        for prijelaz in lista_prijelaza:
            if(prijelaz[0][0] == trenutno_stanje and prijelaz[0][1] == '$' and prijelaz[0][2] == stog[0] and trenutno_stanje not in prihvatljiva_stanja):
                trenutno_stanje = prijelaz[1][0]
                stog = stog[1:len(stog)]
                if(prijelaz[1][1] == '$'):
                    stog = '$'
                else:
                    stog = prijelaz[1][1] + stog 
                print(trenutno_stanje,"#",stog,sep='',end="|")
                


        if(flag == False):
            print("fail", end = "|")
            break
        

    if(trenutno_stanje in prihvatljiva_stanja and flag == True):
        print("1")
    else:
        print("0")