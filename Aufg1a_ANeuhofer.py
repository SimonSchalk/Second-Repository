# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:13:57 2019

@author: Alexander Neuhofer


"""

def is_prime():
    """ Prueft, ob Eingabe eine Primzahl ist. 
        Die Eingabe muss eine Zahl und größer 1 sein, andernfalls wird 
        die Zahl als 'keine Primzahl' bezeichnet """
    
    # Wert abfragen
    Eingabe = int(input("Geben Sie die zu pruefende Zahl ein: "))
    
    # Schleifenzaehler für Schein-Primzahlen
    p = 1
    
    # Ergebnis berechnen
    if Eingabe > 1:
        for i in range(2,Eingabe):
            if (Eingabe % i) != 0:
                p += 1
                #break
            
            else:
                print("Die Zahl ",Eingabe," ist keine Primzahl!")
                p = 0
                break
            
        if p > 1:
            print("Die Zahl ",Eingabe," ist wirklich eine Primzahl!")
     
    # Falls Zahl kleiner 1 eingegeben wurde
    else:
        print("Zahl muss größer 1 sein!")


#### main() ####
is_prime()