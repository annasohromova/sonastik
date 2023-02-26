from модуль1 import *

laused=[] 
while True:
    est=finl('est.txt');rus=finl('rus.txt')
    menu=input("""
1-Sõnade tõlkimine \n2-Vaata sõnastikku \n3-Parandage viga sõnastikus
""")
    while menu.isdigit()==False:
        menu=input("Kirjuta ainult need numbrid, mis on ")
    print()
    if menu=="1":
        tolk(rus,est)
    elif menu=="2":
        laused=loe("rus.txt")
        for line in laused:
            print(line)
        print()
        laused=loe("est.txt")
        for line in laused:
            print(line)
    elif menu=="3":
        paranda("rus.txt","est.txt")
