from functions import *

loadRealEastates()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        printAllRealEsstates()
    elif choice=='2':
        RealEstatesforRent()
    elif choice=='3':
        KeresesTipus()
    elif choice=='4':
        OlcsoLakas()
    elif choice=='5':
        DragaLakas()