#I DIZIONARI DI FUNZIONE

def forward(x):
    print(f"Il robot si muove in avanti di {x} metri") #f-string


def backward(x):
    print(f"Il robot si muove indietro di {x} metri")


def left(x):
    print(f"Il robot si muove a sinistra di {x} metri")


def right(x):
    print(f"Il robot si muove a destra di {x} metri")


def main():

    lista_movimento= [("f", 50), ("f", 10),("r", 20), ("f", 10),("l", 60)]
    #tupla:  (a, b, c...........)
    dizionario_funzioni = {"f": forward, "b": backward, "l": left, "r":right}
    for movimento, valore in lista_movimento:
        dizionario_funzioni[movimento](valore)



if __name__=="__main__":
    main()

