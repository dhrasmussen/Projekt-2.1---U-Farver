import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

tid=0.2
tid2=3

def gravby():


    Landsby = 300 #kr pr m
    Storby = 750 #kr pr m
    Landevej = 100 #kr pr m
    Underboring = 1000 #kr pr m


    taller=3

    time.sleep(tid)

    print("")
    print("Du har valgt udgravning by")
    print("Udfyld felterne her under med værdier")
    print("")

    time.sleep(tid)

    vej = int(input("Indtast antal meter landevej: "))
    land = int(input("Indtast antal meter landsby: "))
    strby = int(input("Indtast antal meter storby: "))
    ubor = int(input("Indtast antal meter underboring: "))

    landevej = vej*Landevej
    landsby = land*Landsby
    storby = strby*Storby
    underboring = ubor*Underboring

    totalpris = str(landevej+landsby+storby+underboring)

    time.sleep(tid)

    print("")
    print("Prisen for landevej", landevej,"kr")
    print("Prisen for landsby", landsby,"kr")
    print("Prisen for storby", storby,"kr")
    print("Prisen for underboring", underboring,"kr")
    print("")
    print("Samlet pris", totalpris, "kr inkl. moms")
    print("")

    time.sleep(tid2)





#print(color.BOLD + 'Hello World !' + color.END)

