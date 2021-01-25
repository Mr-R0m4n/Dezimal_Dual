
#Umrechnung vom Dezimal- in das Dualsystem


zahl = 0
zwischenergebnis = 0
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


