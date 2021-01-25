
#Umrechnung vom Dezimal- in das Dualsystem

loop = True

while loop == True:
    
    zahl = 0
    dual = ""
    eingabe = False
    
    while eingabe == False:
        try:
            zahl = int(input("Geben Sie den Wert als ganze Zahl ein, der umgerechnet werden soll: "))
        except ValueError:
            print("Die Eingabe war nicht gültig")
        else:
            eingabe = True
    
    while zahl != 0:
        dual = str(zahl % 2) + dual
        zahl = zahl // 2
    print(dual)
    
    print()
    print("Möchten Sie das Programm Wiederholen? ")
    print("1 = Ja // 2 = nein")
    redo = int(input("Ihre Auswahl? "))
    print()
    if redo == 1:
        loop = True
    elif redo == 2:
        loop = False
    else:
        print("Ihre Eingabe ist ungültig!")
                  


