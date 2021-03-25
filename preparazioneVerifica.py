#Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a casa. Purtroppo Bob soffre di momentanee perdite di memoria!
#Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la seguente strategia per tentare di rientrare a casa. Ogni minuto decide a caso tra:
#procedere 10 m verso Nord
#procedere 10 m verso Sud
#procedere 10 m verso Est
#procedere 10 m verso Ovest
#Simulare l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia coordinate (0,0) e salvarlo all’interno di un dizionario opportunamente strutturato.
#Disegnare il percorso compiuto da Bob dentro una schermata di pygame.
#Infine salvare il percorso di Bob dentro un file .csv opportunamente strutturato.

#BONUS: ogni volta in cui Bob passa in un punto della città di Flatland in cui è già passato, stampare a schermo le coordinate del punto.

import random
import pygame
import sys
import csv

DIMMAX= 60

dizioPos= {1:[0,0]}

NERO = (0, 0, 0 )       #rgb (x, y, z) -> 0 <= x,y,z => 255 
BIANCO = (255, 255, 255)
BLU = (0,0,255)

dimensione=15
ALTEZZA = dimensione * DIMMAX
LARGHEZZA = dimensione * DIMMAX



def disegnaPercorso():
  
    for k in range(DIMMAX):

        posizione= pygame.Rect((dizioPos[k][0])*dimensione, (dizioPos[k][1])*dimensione,dimensione, dimensione)
        pygame.draw.rect(screen, BLU, posizione)
      


def disegnaGriglia():
    for x in range(0,LARGHEZZA, dimensione):
        for y in range(0, ALTEZZA, dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione)  #vertice alto-sinsitra, max lato
            bordo= pygame.Rect(x,y,dimensione,dimensione) #bordo delle caselle
            pygame.draw.rect(screen, NERO, piastrella)  #dove disegnare, colore, cosa, bordo (se nn metto niente o 0 fa disegno pieno)
            pygame.draw.rect(screen, BIANCO, bordo,1)


def main():
    global screen
    pygame.init()  #parte pygame
    screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))  #dimensioni schermo
    screen.fill(NERO)
    cordX=0
    cordY=0 

    
    
    with open('percorso.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["indice", "coordinata x", "coordinata y"])

    for k in range(DIMMAX):
        val= random.randint(1, 4)

        if val==1:      #vai in su
            cordX+=1

        elif val==2:    #va a destra
            cordY+=1

        elif val==3:    #va in basso
            cordX-=1

        elif val==4:    #va a sinistra
            cordY-=1

        dizioPos[k+1]=[cordX,cordY]


    

    disegnaGriglia()

    while True:
        disegnaPercorso()

    



    pygame.display.update()

   

if __name__ == "__main__":
    main()





