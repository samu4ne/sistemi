#un robot si deve muovere all'interno di una stanza con delle piastrelle, nella stanza ci sono degli
#ostacoli, le piastrelle vengono memorizzate con una matrice(lista di liste), e le celle possono
#essere o libere o occupate. il robot deve arrivare all'arrivo con meno passi

import sys

def main(): 
    pavimento = [[0, 0, 0, -1, -1, 0, -1], #0 libero -1 occupato
                [-1, 0, 0, 0, -1, -1, 0], 
                [0, 0, -1, -1, -1, 0, 0], 
                [-1, 0, 0, 0, -1, -1, 0], 
                [-1, 0, 0, 0, 0, -1, -1], 
                [-1, -1, -1, 0, 0, 0, -1]]  


    dizCoord = {}

    contCelle = 0

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            if pavimento[contY][contX] == 0:             
                pavimento[contY][contX] = contCelle
                contCelle += 1

    spazLiberi = []

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            if pavimento[contY][contX] != -1:

                if contY != 0:      #controllo sinsitra
                    if pavimento[contY - 1][contX] != -1:
                        spazLiberi.append(pavimento[contY - 1][contX])
                    
                if contX != 0:  #controllo destra
                    if pavimento[contY][contX - 1] != -1:
                        spazLiberi.append(pavimento[contY][contX - 1])

                if contX != (len(pavimento[contY]) - 1):    #controllo basso
                    if pavimento[contY][contX + 1] != -1:
                        spazLiberi.append(pavimento[contY][contX + 1])


                if contY != (len(pavimento) - 1):       #controllo alto
                    if pavimento[contY + 1][contX] != -1:
                        spazLiberi.append(pavimento[contY + 1][contX])

                dizCoord[pavimento[contY][contX]] = spazLiberi
                spazLiberi = []
    
    print(dizCoord)

if __name__ == "__main__":
    main()