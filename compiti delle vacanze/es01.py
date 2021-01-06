import random



def generaPasswordEasy():
    caratteri=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    password= ''
    for k in range(0, 8):
        password += random.choice(caratteri)
    return password;

def generaPasswordCompli():
    caratteri=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    password= ''
    for k in range(0, 20):
        password += random.choice(caratteri)
    return password



print("premere \n1:password semplice\n2:password complicata")
lunghezza= input()
if(lunghezza==1):
    password= generaPasswordEasy()
    print(password)
else:
    password= generaPasswordCompli()
    print(password)