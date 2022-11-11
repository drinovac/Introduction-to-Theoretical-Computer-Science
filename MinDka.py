from re import X
import sys

from numpy import append



def pronadi_istovjetna(L, i, j):
    stanje_prijelaz_i = {}
    stanje_prijelaz_j = {}
    for prijelaz in prijelazi:
        if(istovj_lista[i] == prijelaz[0]):
            stanje_prijelaz_i[prijelaz[1]] = prijelaz[2]
        if(istovj_lista[j] == prijelaz[0]):
            stanje_prijelaz_j[prijelaz[1]] = prijelaz[2]
    
    istovjetni = True
    for lista_istih in L:
        for clan_i in stanje_prijelaz_i.keys():
            for clan_j in stanje_prijelaz_j.keys():
                if(clan_i == clan_j and (stanje_prijelaz_i[clan_i] not in lista_istih and stanje_prijelaz_j[clan_j] in lista_istih or 
                                            stanje_prijelaz_i[clan_i] in lista_istih and stanje_prijelaz_j[clan_j] not in lista_istih)):
                    istovjetni = False
    return istovjetni

polje = []
i = 0
for line in sys.stdin:
    polje.insert(i, line)
    i = i + 1


stanja = polje[0].strip()
ulazi = polje[1].strip()
prihvatljiva = polje[2].strip()
poc_stanje = polje[3].strip()
prijelazni = polje[4:]

stanja = stanja.split(',')
ulazi = ulazi.split(',')
prihvatljiva = prihvatljiva.split(',')


lista_prijelaza = []

for line in prijelazni:
    line = line.strip()
    line = line.split('->')
    unutarnja_lista = []
    poc_ul = line[0].split(',')
    unutarnja_lista.append(poc_ul[0])
    unutarnja_lista.append(poc_ul[1])
    unutarnja_lista.append(line[1])
    lista_prijelaza.append(unutarnja_lista)

lista_dohvatljivih = []
lista_dohvatljivih.append(poc_stanje)

for i in lista_dohvatljivih:
    for j in lista_prijelaza:
        if(i == j[0] and j[2] not in lista_dohvatljivih):
            lista_dohvatljivih.append(j[2])

lista_dohvatljivih.sort()
dohvatljiva_prihvatljiva = []
for i in prihvatljiva:
    if(i in lista_dohvatljivih):
        dohvatljiva_prihvatljiva.append(i)
prihvatljiva = dohvatljiva_prihvatljiva
#prijelazi iskljucivo iz dohvatljivih stanja
prijelazi = []
for i in lista_dohvatljivih:
    for j in lista_prijelaza:
        if(i == j[0]):
            prijelazi.append(j)

neprihvatljiva = []
for i in lista_dohvatljivih:
    if i not in prihvatljiva:
        neprihvatljiva.append(i)

L = []
if(neprihvatljiva):
    L.append(neprihvatljiva)
if(prihvatljiva):
    L.append(prihvatljiva)

flag = True
while(flag):
    flag = False
    novi_L = []
    for istovj_lista in L:
        if(len(istovj_lista) == 1):
            novi_L.append(istovj_lista)
        else:
            posebna_lista = []
            novonastala_lista = []
            for i in range(0, len(istovj_lista)):
                
                for j in range(i + 1, len(istovj_lista)):
                    jesu_li = pronadi_istovjetna(L, i, j)
                    if(jesu_li == False):
                        flag = True
                        if(istovj_lista[i] not in posebna_lista):
                            posebna_lista.append(istovj_lista[i])
                        novonastala_lista.append(istovj_lista[j])   
                    else:
                        if(istovj_lista[i] not in posebna_lista):
                            posebna_lista.append(istovj_lista[i])
                        posebna_lista.append(istovj_lista[j])

                       
                if(flag):
                    break
            novi_L.append(posebna_lista)
            if(novonastala_lista):
                novi_L.append(novonastala_lista)
        L = novi_L


for j in novi_L:
    if(len(j) > 1):
        for k in range(1,len(j)):
            for i in prijelazi:
                if(j[k] == i[2]):
                    i[2] = j[0]
            if(j[k] == poc_stanje):
                poc_stanje = j[0]

zavrsna_stanja = []
for i in novi_L:
    zavrsna_stanja.append(i[0])
zavrsna_stanja.sort()
print(*zavrsna_stanja, sep=",")

print(*ulazi, sep=",")
zavrsna_prihvatljiva = []
for i in zavrsna_stanja:
    if(i in prihvatljiva):
        zavrsna_prihvatljiva.append(i)
print(*zavrsna_prihvatljiva, sep=",")
print(poc_stanje)
for i in zavrsna_stanja:
    for prijelaz in prijelazi:
        if(i == prijelaz[0]):
            print(prijelaz[0],",", prijelaz[1], "->" ,prijelaz[2], sep="")