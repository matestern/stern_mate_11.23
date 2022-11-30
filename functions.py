from data import realestates
from os import system
 
filename='ingatlanok.csv'

def menu():
    system('cls')
    print('0 - kilépés')
    print('1 - listázás')
    print('2 - Hirdetés típusa')
    return input('Kérem válasszon: ')

def loadRealEastates():
    file=open(filename,'r',encoding='utf-8')
    global cimsor
    cimsor=file.readline().strip()
    for row in file:
         splitted=row.strip().split(';')
         realestates[splitted[0]]=(splitted[1])
    file.close()

def printAllRealEsstates():
    system('cls')
    print('Ingatlanok Listája:\n')
    for key,value in realestates.items(): 
        print(f'{key} - {value} Ft.')
    input('Tovább...')

def RealEstatesforRent():
    system('cls')
    print('KIadó ingatlanok listája:\n')
    for key,type in realestates.items():
        print(f'{key} - {type} ')
    input('Tovább.....')
    

