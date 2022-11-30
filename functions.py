from data import *
from os import system
 
filename='ingatlanok.csv'

def menu():
    system('cls')
    print('0 - kilépés')
    print('1 - listázás')
    print('2 - Kiadó ingatlanok')
    print('3 - Lakás vagy családiház')
    print('4 - Melyik a legolcsóbb lakás')
    return input('Kérem válasszon: ')

def loadRealEastates():
    file=open(filename,'r',encoding='utf-8')
    file.readline()
    for row in file:
         splitted=row.strip().split(';')
         helye.append(splitted[0])
         ar.append(int(splitted[1]))
         haz.append(splitted[3])
         hirdetés.append(splitted[2])
    file.close()

def printAllRealEsstates():
    system('cls')
    print('Ingatlanok Listája:\n')
    for i in range(0,len(helye)):
        print(f'\t{helye[i]} , {ar[i]} Ft {haz[i]} {hirdetés[i]}')
    input('Tovább...')

def RealEstatesforRent():
    system('cls')
    print('Kiadó ingatlanok listája:\n')
    for i in range(len(hirdetés)):
        if hirdetés[i]=="kiadó":
            print(f'{helye[i]} , {ar[i]} Ft {haz[i]}')
    input('Tovább.....')

def KeresesTipus():
    system('cls')
    print('Ingatlan szűrés típus alapján\n')
    vevo=(input('\tKérem adja meg mi iránt érdeklődik: '))
    for i in range(len(haz)):
        if haz[i]==vevo:
            print(f'{helye[i]} , {ar[i]} Ft {haz[i]}')
    input('Tovább.....')

def OlcsoLakas():
    system('cls')
    print('A legolcsóbb lakás: ')
    minpoz=0
    for i in range(len(ar)):
        if ar[i]<ar[minpoz]:
            minpoz=i
            print(f'{helye[i]} , {ar[minpoz]} Ft {haz[i]}')
    input("Tovább......")

def OlcsoLakas():
    system('cls')
    print('A legolcsóbb lakás: ')
    maxpoz=0
    for i in range(len(ar)):
        if ar[i]>ar[maxpoz]:
            maxpoz=i
            print(f'{helye[i]} , {ar[maxpoz]} Ft {haz[i]}')
    input("Tovább......")
    
    


