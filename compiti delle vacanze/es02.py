#es 02: generare codice_mac
import random

def genera_mac():
    caratteri=('ABCDEF0123456789')
    mac= ''
    for k in range(1, 18):
        if(k%3==0):
            mac += ':'
        else:
            mac += random.choice(caratteri)
    return mac;



indirizzo_mac= genera_mac()
print(indirizzo_mac);