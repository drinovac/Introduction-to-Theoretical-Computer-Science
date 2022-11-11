from pickle import TRUE
from re import X
import sys

from numpy import append

i = 0

def C(ulaz):
    print("C", end="")
    global i
    prvi = A(ulaz)
    drugi = False
    if(i == len(w)-1):
        return False
    if(ulaz == '\n'):
        return True 
    if(prvi == True):
        drugi = A(ulaz)
    if(prvi == False and i != len(w)-2):
        i = i + 1
        ulaz = w[i]
    return drugi

def A(ulaz):
    print("A", end="")
    global i
    if(i == len(w) and w[i] != '\n'):
        return False
    if(w[i] == 'b'):
        i = i + 1
        ulaz = w[i]
        return C(ulaz)
    elif(w[i] == 'a'):
        i = i + 1
        ulaz = w[i]
        return True
    elif(ulaz == '\n'):
        return True
    else:
        return False
    
def B(ulaz):
    global i
    print("B", end="")
    
    if(i == len(w) and w[i] != '\n'):
        return False
    if(w[i] == 'c' and w[i+1] == 'c'):
        i = i + 2
        ulaz = w[i]
        if(S(ulaz) == True and w[i] == 'b' and w[i+1] == 'c'):
            i = i + 2
            ulaz = w[i]
            return True
    elif(ulaz == '\n'):
        return True
    else:
        return True

def S(ulaz):
    print("S", end="")
    global i
    if(i == len(w) and w[i] != '\n'):
        return False
    if(ulaz == 'a'):
        i = i + 1
        ulaz = w[i]
        return A(ulaz) and B(ulaz)
    elif(ulaz == 'b'):
        i = i + 1
        ulaz = w[i]
        return B(ulaz) and A(ulaz)
    elif(ulaz == '\n'):
        return True
    return False
    
    
polje = []
ind = 0
for line in sys.stdin:
    polje.insert(ind, line)
    ind = ind + 1

w = polje[0]


ulaz = w[i]


kraj = S(ulaz)


i = i + 1


if(kraj == False or i != len(w)):
    print("\nNE")
else:
    print("\nDA")
