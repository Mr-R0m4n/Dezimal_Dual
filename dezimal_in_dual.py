"""**************************************
Umrechnung vom Dezimal- in das Dualsystem
**************************************"""

zahl = 0
zwischenergebnis = 0
dual = ""
zahl = int(input("Geben Sie den Wert ein, der umgerechnet werden soll: "))

while zahl != 0:
    zwischenergebnis = zahl // 2
    dual = str(zahl % 2) + dual
    zahl = zwischenergebnis
print(dual)


