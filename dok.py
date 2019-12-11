import fibermm
import fibersm
import udgravningby

global linksmfiber1310
global linksmfiber1550

if __name__ == "__main__":
    File_navn=input("Indtast navnet på opgaven! - HUSK '.txt'")
    f = open(File_navn, "w") #Filen oprettes og hvis der eksistere en i forvejen overskrives den!

    string1=input("Ansvarlig: ")
    string1=string1+"\n"+File_navn # \n laver en ny line i filen
    f.write(string1) #string1 skrives til filen
    f.close() # Filen lukkes ned

    f = open(File_navn, "a") # Filen åbnes og nu kan der adder noget tekst til den
    string1=input("Single Mode: ")
    string1=string1+"\n" # \n laver en ny line i filen
    f.write(string1)

    string2=input("Multi Mode: ")
    string2=string2+"\n" # \n laver en ny line i filen
    f.write(string2)

    string3=input("Udgravningspris: ")
    string3=string3+"\n" # \n laver en ny line i filen
    f.write(string3)
    f.close()






    #taller=10

    #print("Single Mode 1310 mediekonverter ", linksmfiber1310,"dB")
    #print("Single Mode 1550 mediekonverter ", linksmfiber1550,"dB")
    #print("Multi Mode 850 mediekonverter ", linkmmfiber850,"dB")
    #print("Multi Mode 1500 mediekonverter  ", linkmmfiber1300,"dB")
    #print("")

    #print("Prisen for landevej", landevej,"kr")
    #print("Prisen for landsby", landsby,"kr")
    #print("Prisen for storby", storby,"kr")
    #print("Prisen for underboring", underboring,"kr")
    #print("")
    #print("Samlet pris", totalpris,"kr inkl. moms")
    #print("")


