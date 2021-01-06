import string

def ROT15_crip(stringa):
    for k in range(len(stringa)):
        temp=ord(stringa[k])  #restituisce il codice ascii di una lettera e la assegna ad una variabile
        if(temp<=107):
            temp=temp+15
            print(chr(temp)) #restituisce la lettera e la stampa
        else:
            temp=97+(122-temp)
            print(chr(temp)) #restituisce la lettera e la stampa


def ROT15_decrip(stringa):
    for k in range(len(stringa)):
        temp=ord(stringa[k])  #restituisce il codice ascii di una lettera e la assegna ad una variabile
        if(temp>=112):
            temp=temp-15
            print(chr(temp)) #restituisce la lettera e la stampa
        else:
            temp=122-(temp-97)
            print(chr(temp)) #restituisce la lettera e la stampa




print("premere:\n1:criptare\n2:decriptare")
n=input()
if(n==1):
    stringa=input("inserire la stringa da criptare")
    ROT15_crip(stringa)
else:
    stringa=input("inserire la stringa da decriptare")
    ROT15_decrip(stringa)