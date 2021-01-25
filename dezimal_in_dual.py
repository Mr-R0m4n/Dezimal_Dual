"""**************************************
Umrechnung vom Dezimal- in das Dualsystem
**************************************"""

zahl = 0
zwischenergebnis = 0
txt = ""

zahl = int(input("Geben Sie den Wert ein, der umgerechnet werden soll: "))

while zahl != 0:
    zwischenergebnis = zahl // 2
    binaer = str(zahl % 2) + txt
    zahl = zwischenergebnis
print(binaer)


