'''Nel file instagram.csv trovate alcuni dati esportati dal vostro account Instagram. 
Ogni riga del file corrisponde ad un post pubblicato nel 2020 e su ogni riga trovate in ordine:
 mese, giorno del mese, identificativo del post, numero di like.

Scrivere un programma in Python che 
1) crei un dizionario in cui le chiavi siano tutti i mesi dell'anno ed i valori siano i totali dei 
    like per quel mese.
2) richieda all'utente il nome di un mese e poi fornisca in output il numero di post di quel mese 
    ed il numero totale di like ricevuto durante quel mese.
'''
import random
import pygame
import sys
import csv
import array

dizionario={}

def main():

    with open("/home/samuele/Scrivania/scuola/4/tpsit/pyton/instagram/instagram.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv,delimiter=",")
        fatto= False
        for temp in lettore:
            if(fatto):
                if(temp[0] in dizionario):
                    dizionario[temp[0]][0]+= int(temp[3])
                    dizionario[temp[0]][1]=dizionario[temp[0]][1]+1
                else:
                    dizionario[temp[0]]=[int(temp[3]),1]
            fatto=True   
    mese=input("inserisci il mese ")

    if (mese in dizionario):
        print(f"{dizionario[mese][0]} {dizionario[mese][1]}" )
    else:
        print("non esiste")
    
    
            

    

if __name__=="__main__":
    main()