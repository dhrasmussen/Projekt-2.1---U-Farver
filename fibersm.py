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
linksmfiber1550=0
linksmfiber1310=0

def udregnsm():
    global linksmfiber1310
    global linksmfiber1550

    konnektering = 0.5 #db
    splidsning = 0.1 #db 1 pr 4km # (km/4)*0.1=
    smfiber1310 = 0.35 #db/km
    smfiber1550 = 0.2 #db/km
    mmfiber850 = 2.2 #db/km
    mmfiber1300 = 0.6 #db/km
    sikkerhedsmargin = 1 #pr 10km
    fastsikkerhedmargin = 3 #fast værdi
    reperarion = 0.5 #fast værdi

    taller=1
    time.sleep(tid)
    print("")
    print("Du har valgt Single Mode Fiber")
    print("Udfyld felterne her under med værdier")
    print(" ")
    print("Som standart er der lagt følgende ind i udregningen")
    print("- Reperation: 1 stk")
    print("- Sikkerhedsmargin")
    print(" ")
    print("Følgende værdier er sat til")
    print("- Sikkerhedsmargin 3dB")
    print("- Konnekteringer 0,5dB")
    print("- Splidsning 0,1dB")
    print("- Reperation 0,5dB")
    print("")
    print("Udregningerne på Single Mode er lavet ud fra worst case")
    print("- Attenauation at 1310nm 0,35dB/km")
    print("- Attenauation at 1550nm 0,21dB/km")
    print("")
    time.sleep(tid)
    km = float(input("Indtast tallet for km: "))
    splidsninger = int(input("Indtast antal forventet splidsninger: "))
    konnekteringer = int(input("Indtast antal forventet konnekteringer: "))
    time.sleep(tid)

    kmsmfiber1310 = km*smfiber1310
    kmsmfiber1550 = km*smfiber1550
    #print("kmsm1312", kmsmfiber1310)
    #print("kmsm1550", kmsmfiber1550)

    splidsningsm1310 = km/4*0.1
    splidsningsm1550 = km/4*0.1
    #print("splids1310", splidsningsm1310)
    #print("splids1550", splidsningsm1550)

    konnekteringsm1310 = konnekteringer*0.5
    konnekteringsm1550 = konnekteringer*0.5
    #print("Kone1310", konnekteringsm1310)
    #print("Kone1550", konnekteringsm1550)

    sikmargin = km/10
    #print("sikmargin", sikmargin)

    fast_værdi = reperarion + fastsikkerhedmargin
    #print("fast_værdi", fast_værdi)

    linksmfiber1310 = round(konnekteringsm1310+splidsningsm1310+kmsmfiber1310+sikmargin+fast_værdi, 2)
    #print("links1310", linksmfiber1310)

    linksmfiber1550 = round(konnekteringsm1550+splidsningsm1550+kmsmfiber1550+sikmargin+fast_værdi, 2)
    #print("links1550", linksmfiber1550)

    print("")
    print("Ved brug af SM1310 skal den valgte mediekonverter understøtte ", str(linksmfiber1310), "dB")
    print("Ved brug af SM1550 skal den valgte mediekonverter understøtte ", str(linksmfiber1550), "dB")
    print("")

    time.sleep(tid2)
